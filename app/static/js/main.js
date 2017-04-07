(() => {
  const facebookLoginUrl = window.facebookLogin;
  const googleLoginUrl = window.googleLogin;

  $('.btn-facebook').on('click', evt => {
    FB.login(response => {
      if (response.status == 'connected') {
        $.post(facebookLoginUrl, {
          token: response.authResponse.accessToken
        })
        .done(_ => document.location.reload());
      } else {
        console.error(response);
      };
    }, {scope: 'public_profile,email'});
  });

  $('.btn-google').on('click', evt => {
    // pass
  });
})()
