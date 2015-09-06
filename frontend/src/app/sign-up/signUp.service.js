(function() {
  'use strict';

  angular
    .module('frontend')
    .factory('SignUpService', SignUpService);

  /** @ngInject */
  function SignUpService($log, $http, toastr) {
    var apiHost = 'http://127.0.0.1:5000';

    var service = {
      apiHost: apiHost,
      signUp: signUp
    };

    return service;

    function signUp(email, password) {
      var requestData = JSON.stringify({
        email: email,
        password: password
      });

      console.log(requestData);

      return $http.post(apiHost + '/api/new_user', requestData)
        .then(postNewUserSuccess)
        .catch(postNewUserFailed);

      function postNewUserSuccess(response) {
        return { 
          data: response.data, 
          success: true
        }
      }

      function postNewUserFailed(error) {
        var errorMsg;
        if (error.status === 400) {
          errorMsg = "Юзер з такими параметрами вже існує";
        } else {
          errorMsg = "Проблеми з сервером. Спробуйте пізніше";
        }
        $log.error("Error while creating new user");
        return { 
          data: error,
          success: false,
          errorMsg: errorMsg
        }
      }
    }
  }
})();
