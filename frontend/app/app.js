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
        // http://paletton.com/#uid=1460u0kk2t7adKLfAzEoiq2rwkR
        var customPrimary = {
            '50': '#a099d1',
            '100': '#8f87c9',
            '200': '#7f76c1',
            '300': '#6f64b9',
            '400': '#5e53b1',
            '500': '#5449A1',
            '600': '#4b418f',
            '700': '#42397e',
            '800': '#39316c',
            '900': '#2f295b',
            'A100': '#b0aad9',
            'A200': '#c0bce1',
            'A400': '#d1cde9',
            'A700': '#262149'
        };
        $mdThemingProvider
            .definePalette('customPrimary',
            customPrimary);

        var customAccent = {
            '50': '#7d72cf',
            '100': '#6c5fc8',
            '200': '#5b4cc2',
            '300': '#4d3eb6',
            '400': '#4537a3',
            '500': '#3D3190',
            '600': '#352b7d',
            '700': '#2d246a',
            '800': '#251e57',
            '900': '#1d1744',
            'A100': '#8f85d5',
            'A200': '#a098dc',
            'A400': '#b2abe2',
            'A700': '#151131'
        };
        $mdThemingProvider
            .definePalette('customAccent',
            customAccent);

        var customWarn = {
            '50': '#f7f7fc',
            '100': '#e6e5f4',
            '200': '#d6d2ed',
            '300': '#c5c0e6',
            '400': '#b4aede',
            '500': '#A39CD7',
            '600': '#928ad0',
            '700': '#8178c8',
            '800': '#7066c1',
            '900': '#5f53ba',
            'A100': '#ffffff',
            'A200': '#ffffff',
            'A400': '#ffffff',
            'A700': '#5246ad'
        };
        $mdThemingProvider
            .definePalette('customWarn',
            customWarn);

        var customBackground = {
            '50': '#f7f7fc',
            '100': '#e6e5f4',
            '200': '#d6d2ed',
            '300': '#c5c0e6',
            '400': '#b4aede',
            '500': '#A39CD7',
            '600': '#928ad0',
            '700': '#8178c8',
            '800': '#7066c1',
            '900': '#5f53ba',
            'A100': '#ffffff',
            'A200': '#ffffff',
            'A400': '#ffffff',
            'A700': '#5246ad'
        };
        $mdThemingProvider
            .definePalette('customBackground',
            customBackground);

        $mdThemingProvider.theme('default')
            .primaryPalette('customPrimary')
            .accentPalette('customAccent')
            .warnPalette('customWarn')
            .backgroundPalette('customBackground');
    });