module.exports = function (grunt) {

    grunt.loadNpmTasks('grunt-karma');
    grunt.loadNpmTasks('grunt-contrib-jshint');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-serve');

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        'meta': {
            'jsFilesForTesting': [
                'bower_components/angular/angular.js',
                'bower_components/angular-route/angular-route.js',
                'bower_components/angular-sanitize/angular-sanitize.js',
                'bower_components/angular-mocks/angular-mocks.js',
                'bower_components/lodash/lodash.js',
                'test/**/*Spec.js'
            ]
        },
        'karma': {
            'development': {
                'configFile': 'karma.conf.js',
                'options': {
                    'files': [
                        '<%= meta.jsFilesForTesting %>',
                        'app/**/*.js'
                    ]
                }
            }
        },

        'jshint': {
            'beforeconcat': ['source/**/*.js']
        },

        'concat': {
            'dist': {
                'src': ['source/**/*.js'],
                'dest': 'dist/<%= pkg.namelower %>-<%= pkg.version %>.js'
            }
        },

        'uglify': {
            'options': {
                'mangle': false
            },
            'dist': {
                'files': {
                    'dist/<%= pkg.namelower %>-<%= pkg.version %>.min.js': ['dist/<%= pkg.namelower %>-<%= pkg.version %>.js']
                }
            }
        }
    });

    grunt.registerTask('build',
        [
            'jshint',
            'concat',
            'uglify'
        ]);


};