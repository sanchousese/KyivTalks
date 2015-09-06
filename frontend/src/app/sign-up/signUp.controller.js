(function() {
  'use strict';

  angular
  .module('frontend')
  .controller('SignUpController', SignUpController);

  /** @ngInject */
  function SignUpController($scope, toastr) {
    var vm              = this;
    
    $scope.email = "";
    $scope.password = "";
    $scope.signUp = function(){
      console.log($scope.email, $scope.password);
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
