(function() {
  'use strict';

  angular
    .module('frontend')
    .config(routeConfig);

  function routeConfig($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: 'app/main/main.html',
        controller: 'MainController',
        controllerAs: 'main'
      })
      .when('/sign_in', {
        templateUrl: 'app/sign-in/sign-in.html',
        controller: 'SignInController',
        controllerAs: 'signIn'
      })
      .when('/sign_up', {
        templateUrl: 'app/sign-up/sign-up.html',
        controller: 'SignUpController',
        controllerAs: 'signUp'
      })
      .otherwise({
        redirectTo: '/'
      });
  }

})();
