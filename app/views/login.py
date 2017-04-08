from decouple import config
from flask import abort, request, jsonify, redirect, url_for
from flask_classy import FlaskView, route
from flask_login import login_user, logout_user
import requests
from ..extensions import login_manager
from ..models import UserModel


@login_manager.user_loader
def user_load(user_id):
    """ Usser loader, requisite for Flask Login. """
    try:
        user = UserModel.query.get(user_id)
        return user
    except Exception as err:
        print(err)
        return None


# Predefined services and request that can be done.
REQUESTS_INFO = {
    'facebook': {
        'access_token': {
            'url': 'https://graph.facebook.com/oauth/access_token',
            'token': 'fb_exchange_token',
            'payload': dict(grant_type='fb_exchange_token',
                            client_id=config("FACEBOOK_CLIENT_ID"),
                            client_secret=config("FACEBOOK_CLIENT_SECRET"),
                            fb_exchange_token='')},
        'user': {
            'url': 'https://graph.facebook.com/me',
            'token': 'access_token',
            'payload': dict(access_token='', fields='id,name,email')},
        'user_picture': {
            'url': 'https://graph.facebook.com/me/picture',
            'token': 'access_token',
            'payload': dict(access_token='', height=200, widht=200)}
    },
    'google': {
        'access_token': {
            'url': 'https://www.googleapis.com/oauth2/v4/token',
            'token': 'code',
            'payload': dict(code='', client_id=config("GOOGLE_CLIENT_ID"),
                            client_secret=config("GOOGLE_CLIENT_SECRET"),
                            grant_type='authorization_code',
                            redirect_uri="http://localhost:5000")},
        'user': {
            'url': 'https://www.googleapis.com/oauth2/v2/userinfo',
            'token': 'access_token',
            'payload': dict(access_token='')}
    }
}

BAD_REQUEST_MSG = {
    'no_token': 'A token field is required.',
    'invalid_token': 'A valid token is required.',
    'user_info': 'Unable to fetch user info.'
}


def get_service(service, request, token):
    """ Given a service and kind of request return url and payload
        fullfit. """
    service = REQUESTS_INFO.get(service)
    if not service:
        return
    requestd = service.get(request)
    if not requestd:
        return
    url = requestd.get('url')
    token_id = requestd.get('token')
    payload = requestd.get('payload')
    payload[token_id] = token
    return url, payload


class Login(FlaskView):

    @route('facebook/', methods=['POST'])
    def facebook(self):
        """ Facebook login endpoint. """
        service = 'facebook'
        token = request.form.get('token', None)
        if token:
            user = self.load_user_info(service, token)
            if isinstance(user, tuple):
                # And error have occur
                return user
            self.login(user)
            return jsonify(logged=True)
        return self.bad_request('no_token')

    @route('google/', methods=['POST'])
    def google(self):
        """ Google login endpoint. """
        service = 'google'
        token = request.form.get('token', None)
        if token:
            user = self.load_user_info(service, token)
            if isinstance(user, tuple):
                # And error have occue
                return user
            self.login(user)
            return jsonify(logged=True)
        return self.bad_request('no_token')

    def load_user_info(self, service, token):
        """ Load user info from a given service. """
        if service == 'google':
            response = self._request_json(service, 'access_token', token,
                                          method="post")
        else:
            response = self._request_json(service, 'access_token', token)
        if not response:
            return self.bad_request('invalid_token')
        token = response['access_token']
        user_info = self._request_json(service, 'user', token)
        if not user_info:
            return self.bad_request('user_info')
        del user_info['id']
        if service == 'facebook':
            picture = self._request(service, 'user_picture', token)
            user_info['picture'] = picture.url if picture else ''
        return user_info

    def login(self, user):
        """ Recive a user info and try to log in it.
            If an user does not exist create it. """
        user = UserModel.query.filter_by(email=user['email']).first()
        if not user:
            user = UserModel.add(name=user['name'], email=user['email'],
                                 picture=user['picture'])
        return login_user(user)

    def logout(self):
        """ Logout a user """
        logout_user()
        return redirect(url_for('Main:index'))

    def bad_request(self, message, code=400):
        """ Return a Json error response. """
        return jsonify(error=BAD_REQUEST_MSG.get(message)), code

    def _request(self, service, request, token, method='get'):
        """ Make a request given a predefined services and kind of requests.
            A method can be specified. If and error happens return None. """
        try:
            request_func = getattr(requests, method)
            if request_func and callable(request_func):
                url, payload = get_service(service, request, token)
                if not url and payload:
                    return
                response = request_func(url, params=payload)
                if response.status_code == requests.codes.ok:
                    return response
            return
        except:
            return

    def _request_json(self, service, request, token, method='get'):
        """ Wrapper for _request, if a response if recived return it as json,
            if able to decode. """
        try:
            r = self._request(service, request, token, method)
            json = r.json()
            return json if json else None
        except:
            return
