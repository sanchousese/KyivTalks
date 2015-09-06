(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('MainController', MainController);

  /** @ngInject */
  function MainController(toastr) {
    var vm = this;

    activate();

    function activate() {
      console.log('Started!');
    }
  }
})();
