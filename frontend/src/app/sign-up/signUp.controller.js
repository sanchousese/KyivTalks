(function() {
  'use strict';

  angular
  .module('frontend')
  .controller('SignUpController', SignUpController);

  /** @ngInject */
  function SignUpController(toastr, SignUpService, $location, $rootScope) {
    var vm = this;
    
    vm.email = "";
    vm.password = "";
    vm.passwordConfirmation = "";

    vm.signUp = function(){
      if (vm.email && vm.password && vm.password === vm.passwordConfirmation) {
        SignUpService.signUp(vm.email, vm.password)
        .then(function(obj){
          if (obj.success) {
            toastr.success("Реєстрація успішна. Виконайте вхід");
            $location.path('/sign_in');
          } else {
            vm.email = "";
            vm.password = "";
            vm.passwordConfirmation = "";
            toastr.error(obj.errorMsg);
          }
        });
      }
      else {
        if (vm.password === vm.passwordConfirmation) {
          toastr.error("Не вистачає параметрів для реєстрації");
        } else {
          toastr.error("Пароль та підтвердження не співпадають");
        }
      }
    };

    activate();

    function activate() {
      console.log('Sign up!');
    }
  }
})();
