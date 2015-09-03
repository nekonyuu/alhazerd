'use strict';

angular.module('alhazerd.gallery', ['ngRoute'])

    .config(['$routeProvider', function ($routeProvider) {
        $routeProvider.when('/gallery', {
            templateUrl: 'gallery/view/gallery.html',
            controller: 'galleryController'
        });
    }]);