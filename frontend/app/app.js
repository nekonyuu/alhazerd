'use strict';

// Declare app level module which depends on views, and components
angular.module('alhazerd', [
    'ngMaterial',
    'ngMdIcons',
    'ngRoute',
    'alhazerd.home',
    'alhazerd.profile',
    'alhazerd.gallery'
]).
    config(['$routeProvider', function ($routeProvider) {
        $routeProvider.otherwise({redirectTo: '/home'});
    }]).
    config(function ($mdThemingProvider, $mdIconProvider) {
        $mdIconProvider
            .icon("login", "./assets/svg/login.svg", 24);

        $mdThemingProvider
            .theme('default')
            .primaryPalette('blue-grey')
            .accentPalette('cyan')
            .warnPalette('red')
            .backgroundPalette('grey');
    });