

(() => {
  const facebookLoginUrl = window.facebookLogin;
  const googleLoginUrl = window.googleLogin;

  $('.btn-facebook').on('click', evt => {
    FB.login(response => {
      if (response.status == 'connected') {
        $.post(facebookLoginUrl, {
          token: response.authResponse.accessToken
        })
        .done(_ => document.location.reload())
        .fail(err => console.log(err.responseText));
      } else {
        console.error(response);
      };
    }, {scope: 'public_profile,email'});
  });

  $('.btn-google').on('click', evt => {

    const singInCallback = (authResponse) => {
      if (authResponse.code) {
        $.post(googleLoginUrl, {
          token: authResponse.code
        })
        .done(_ => document.location.reload())
        .fail(err => console.log(err.responseText));
      } else {
        console.error(authResponse);
      };
    };
    auth2.grantOfflineAccess()
      .then(singInCallback);

  });
})()
