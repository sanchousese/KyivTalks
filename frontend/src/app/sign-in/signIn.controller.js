(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('SignInController', SignInController);

  /** @ngInject */
  function SignInController(toastr) {
    var vm = this;

    activate();

    function activate() {
      console.log('Sign in!');
    }
  }
})();
