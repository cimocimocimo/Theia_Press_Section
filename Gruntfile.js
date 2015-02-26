
module.exports = function(grunt) {

    require('load-grunt-tasks')(grunt);

    // Project configuration.
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),
        sass: {
            dev: {
                options: {                       // Target options
                    style: 'expanded'
                },
                files: {                         // Dictionary of files
                    'press_section/static/base.css': 'press_section/static/base.scss'
                }
            }
        },
        watch: {
            sass: {
                files: 'press_section/static/*.scss',
                tasks: ['sass']
            },
            livereload: {
                files: 'press_section/static/*.css',
                options: {
                    livereload: true
                }
            }
        },
        shell: {
            options: {
                stderr: false
            },
            djangoCompress: {
                command:  './manage.py compress'
            }
        }
    });

    // grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-sass');
    grunt.loadNpmTasks('grunt-contrib-watch');
    
    // Default task(s).
    grunt.registerTask('default', ['watch']);

};
