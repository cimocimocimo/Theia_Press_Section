#!/bin/sh

source /opt/elasticbeanstalk/lib/ruby/profile.sh
python manage.py compress &> /tmp/compress-output
