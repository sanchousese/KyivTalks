(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('SignInController', SignInController);

  /** @ngInject */
  function SignInController($http, $location, API_BASE) {
    var vm = this;

    vm.submit = function() {
      $http.get(API_BASE + '/token', {
        headers: {
          'Authorization': 'Basic ' + btoa(vm.username + ':' + vm.password)
        }
      }).then(function(response) {
        localStorage.setItem('token', data.token);
        console.log('successfully authenticated', response);

        $location.path('/');
      }, function() {
        alert("Can't authenticate!");
      });
    };
  }
})();
