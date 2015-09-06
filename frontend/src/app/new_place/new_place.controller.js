(function() {
  'use strict';

  angular
    .module('frontend')
    .controller('NewPlace', NewPlace);

  /** @ngInject */
  function NewPlace($rootScope, $location, $http, API_BASE) {
    var vm = this;

    vm.newPlaceModel = {
      name: '',
      address: '',
      description: ''
    };

    vm.submit = function() {
      $http.post(
        API_BASE + 'places/new_place',
        vm.newPlaceModel
      ).than(function(result) {
        $location.path('/');
      }, function(error) {
        alert(error);
      });
    };
  }
})();
