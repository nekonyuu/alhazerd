#!/bin/bash

sudo fpm -n alhazerd -v 1.0.1 -a all -C alhazerd -m '<jonathan.raffre@nekolover.net>' --after-install alhazerd/alhazerd.postinstall --description 'Alhazerd Image Upload Manager' --url 'http://www.nekolover.net/' -t deb --config-files etc/alhazerd/settings.py -d python-django -d python-flup -d python-imaging -d python-magic -d python-mysqldb -d python-webpy -s dir etc usr
