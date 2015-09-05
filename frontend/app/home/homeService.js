'use strict';

angular
    .module('alhazerd.home')
    .service('homeService', ['$q', HomeService]);

function HomeService($q) {
    var medias = [
        {
            name: 'Cat 1',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/tWeoyoyKIo24fMe5ON3whsO4F.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/pRZQ93PB75oFVovzUlPhgjCbq.JPG'
        },
        {
            name: 'Cat 2',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/9sclV0CZVd7Dh4YRMVqJklrfv.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/0kat2WDsQAVaA9U0HK8nEk1ug.JPG'
        },
        {
            name: 'Cat 1',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/tWeoyoyKIo24fMe5ON3whsO4F.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/pRZQ93PB75oFVovzUlPhgjCbq.JPG'
        },
        {
            name: 'Cat 2',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/9sclV0CZVd7Dh4YRMVqJklrfv.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/0kat2WDsQAVaA9U0HK8nEk1ug.JPG'
        },
        {
            name: 'Cat 1',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/tWeoyoyKIo24fMe5ON3whsO4F.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/pRZQ93PB75oFVovzUlPhgjCbq.JPG'
        },
        {
            name: 'Cat 2',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/9sclV0CZVd7Dh4YRMVqJklrfv.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/0kat2WDsQAVaA9U0HK8nEk1ug.JPG'
        },
        {
            name: 'Cat 1',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/tWeoyoyKIo24fMe5ON3whsO4F.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/pRZQ93PB75oFVovzUlPhgjCbq.JPG'
        },
        {
            name: 'Cat 2',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/9sclV0CZVd7Dh4YRMVqJklrfv.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/0kat2WDsQAVaA9U0HK8nEk1ug.JPG'
        },
        {
            name: 'Cat 1',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/tWeoyoyKIo24fMe5ON3whsO4F.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/pRZQ93PB75oFVovzUlPhgjCbq.JPG'
        },
        {
            name: 'Cat 2',
            thumbnailLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/thumbnails/9sclV0CZVd7Dh4YRMVqJklrfv.jpg',
            fullsizeLink: 'http://static.nekolover.net/cdn/Alhazerd/uploader/fullsize/0kat2WDsQAVaA9U0HK8nEk1ug.JPG'
        }
    ];

    // Promise-based API
    return {
        loadAllMedias: function() {
            // Simulate async nature of real remote calls
            return $q.when(medias);
        }
    };

}
