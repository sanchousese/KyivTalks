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
        console.log(response.data);
        toastr.success("Success!");
        return { 
          data: response.data, 
          success: true
        }
      }

      function postNewUserFailed(error) {
        if (error.status === 400) {
          toastr.error("User already exists");
        } else {
          toastr.error("Service problems. Try again later.");
        }
        $log.error("Error while creating new user");
        return { 
          data: error,
          success: false
        }
      }
    }
  }
})();
