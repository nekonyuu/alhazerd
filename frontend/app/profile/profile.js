'use strict';

angular.module('alhazerd.profile', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/profile', {
            templateUrl: 'profile/view/profile.html',
            controller: 'profileController'
        });
    }]);