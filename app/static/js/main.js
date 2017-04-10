

(() => {
  // Oauth logins FB and Google
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

  // Delete items
  const deleteItemUrl = window.deleteItemUrl;
  $('.delete-btn').on('click', (evt) => {
    $.ajax(deleteItemUrl, {
      method: 'DELETE'
    })
    .done(_ => window.location.replace("/"))
    .fail(err => console.log(err.responseText));
  });
})()
