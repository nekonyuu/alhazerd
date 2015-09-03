'use strict';

// Declare app level module which depends on views, and components
angular.module('alhazerd', [
    'ngMaterial',
    'ngRoute',
    'alhazerd.home',
    'alhazerd.profile',
    'alhazerd.gallery'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }]).
    config(function($mdThemingProvider){
        $mdThemingProvider.theme('default')
            .primaryPalette('blue-grey')
            .accentPalette('cyan');
    });