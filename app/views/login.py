from decouple import config
from flask import abort, request, jsonify
from flask_classy import FlaskView, route
from flask_login import login_user
import requests
from ..extensions import login_manager
from ..models import UserModel


@login_manager.user_loader
def user_load(user_id):
    try:
        user = UserModel.query.get(user_id)
        return user
    except Exception as err:
        print(err)
        return None


class Login(FlaskView):

    @route('facebook/', methods=['POST'])
    def facebook(self):
        token = request.form.get('token', None)
        if token and self._request_long_token(token) and self._request_user_info():
            user = UserModel.query.filter_by(email=self.user_info['email']).first()
            if not user:
                user = UserModel.add(**self.user_info)
            login_user(user)
            return jsonify(logged=True)
        return abort(501)

    def google(self):
        pass

    def _request_long_token(self, token):
        payload = dict(grant_type='fb_exchange_token',
                       client_id=config("FACEBOOK_CLIENT_ID"),
                       client_secret=config("FACEBOOK_CLIENT_SECRET"),
                       fb_exchange_token=token)
        fb = "https://graph.facebook.com/oauth/access_token"
        response = self.__call(fb, payload)
        if response:
            json = response.json()
            self.long_token = json.get('access_token')
            return self.long_token or None
        return

    def _request_user_info(self):
        payload = dict(access_token=self.long_token, fields='id,name,email')
        fb = "https://graph.facebook.com/me"
        response = self.__call(fb, payload)
        if response:
            self.user_info = response.json()
            del self.user_info['id']
            if self._request_user_profile_picture():
                return True
        return

    def _request_user_profile_picture(self):
        payload = dict(access_token=self.long_token, height=200, widht=200)
        fb = "https://graph.facebook.com/me/picture"
        response = self.__call(fb, payload)
        if response:
            self.user_info['picture'] = response.url
            return True
        return

    def __call(self, url, payload):
        try:
            response = requests.get(url, params=payload)
            if response.status_code == requests.codes.ok:
                return response
            return
        except:
            return
