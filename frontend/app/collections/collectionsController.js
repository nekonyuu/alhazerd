'use strict';

angular
    .module('alhazerd.collections')
    .controller('collectionsController', ['collectionsService', '$scope', '$mdSidenav', CollectionsController]);

function CollectionsController(collectionsService, $scope, $mdSidenav) {
    var self = this;

    $scope.toggleMenu = function () { $mdSidenav('left').toggle(); };
}
