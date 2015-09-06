(function() {
  'use strict';

  angular
  .module('frontend')
  .controller('SignUpController', SignUpController);

  /** @ngInject */
  function SignUpController(toastr, SignUpService, $location) {
    var vm = this;
    
    vm.email = "";
    vm.password = "";
    vm.signUp = function(){
      if (vm.email && vm.password) {
        var result = SignUpService.signUp(vm.email, vm.password);
        console.log(result);
        // if (result.success) {
        //   $location.path('/sign_in');
        // } else {
        //   $location.path('/sign_in');
        // }
      }
      else {
        toastr.error("Не вистачає параметрів для реєстрації");
      }
    };

    activate();

    function activate() {
      console.log('Sign up!');
    }

    // function signUp() {
    //   // SignUpService.signUp(email, password);
    //   console.log($scope.email, $scope.password);
    // }
  }
})();
