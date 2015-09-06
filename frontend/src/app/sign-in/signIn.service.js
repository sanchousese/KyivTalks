// (function() {
//   'use strict';

//   angular
//     .module('frontend')
//     .factory('SignInService', SignInService);

//   /** @ngInject */
//   function SignInService($log, $http, toastr) {
//     var apiHost = 'http://127.0.0.1:5000';

//     var service = {
//       apiHost: apiHost,
//       signIn: signIn
//     };

//     return service;

//     function signIn(email, password) {
//       var requestData = JSON.stringify({
//         email: email,
//         password: password
//       });

//       console.log(requestData);

//       return $http.get(apiHost + '/api/new_user', requestData)
//         .then(postNewUserSuccess)
//         .catch(postNewUserFailed);

//       function postNewUserSuccess(response) {
//         console.log(response.data);
//         toastr.success("Success!");
//         return response.data;
//       }

//       function postNewUserFailed(error) {
//         toastr.error("Error!");
//         $log.error("Error while creating new user");
//       }
//     }
//   }
// })();
