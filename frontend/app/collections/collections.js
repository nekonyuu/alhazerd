'use strict';

angular.module('alhazerd.collections', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/collections', {
            templateUrl: 'collections/view/collections.html',
            controller: 'collectionsController'
        });
    }]);