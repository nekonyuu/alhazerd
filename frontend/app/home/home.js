'use strict';

angular.module('alhazerd.home', ['ngMaterial', 'ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/home', {
            templateUrl: 'home/view/home.html',
            controller: 'homeController'
        });
    }]);
