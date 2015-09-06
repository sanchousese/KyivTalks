(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('SignUpController', SignUpController);

  /** @ngInject */
  function SignUpController(toastr) {
    var vm = this;

    activate();

    function activate() {
      console.log('Sign up!');
    }
  }
})();
