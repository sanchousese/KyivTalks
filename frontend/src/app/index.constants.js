/* global malarkey:false, toastr:false, moment:false */
(function() {
  'use strict';

  angular
    .module('frontend')
    .constant('malarkey', malarkey)
    .constant('toastr', toastr)
    .constant('moment', moment)
    .constant('API_BASE', 'http://127.0.0.1:5000/api/');

})();
