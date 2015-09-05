'use strict';

angular
    .module('alhazerd.profile')
    .controller('profileController', ['profileService', '$scope', '$mdSidenav', ProfileController]);

function ProfileController(profileService, $scope, $mdSidenav) {
    var self = this;

    $scope.toggleMenu = function () { $mdSidenav('left').toggle(); };
}
