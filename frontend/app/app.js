'use strict';

// Declare app level module which depends on views, and components
angular.module('alhazerd', [
    'ngMaterial',
    'ngMdIcons',
    'ngRoute',
    'alhazerd.home',
    'alhazerd.profile',
    'alhazerd.collections'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }]).
    config(function ($mdThemingProvider, $mdIconProvider) {
        $mdThemingProvider
            .theme('default')
            .primaryPalette('blue-grey')
            .accentPalette('cyan')
            .warnPalette('red')
            .backgroundPalette('grey');
    });