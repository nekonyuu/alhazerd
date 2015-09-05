'use strict';

angular
    .module('alhazerd.home')
    .controller('homeController', ['homeService', '$scope', '$mdSidenav', HomeController]);

function HomeController(homeService, $scope, $mdSidenav) {
    var self = this;

    self.medias = [];

    $scope.toggleMenu = toggleMenu;

    $scope.loadMedias = loadMedias;

    homeService.loadAllMedias().then(function (medias) {
            self.medias = [].concat(medias);
        }
    );

    function toggleMenu() {
        $mdSidenav('left').toggle();
    }

    function loadMedias() {
    }
}
