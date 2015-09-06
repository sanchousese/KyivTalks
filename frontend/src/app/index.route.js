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
        templateUrl: 'app/sign_in/sign_in.html'
      })
      .when('/new_place', {
        templateUrl: 'app/new_place/new_place.html',
        controller: 'NewPlace',
        controllerAs: 'newPlace'
      })
      .otherwise({
        redirectTo: '/'
      });
  }

})();
