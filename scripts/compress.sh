#!/bin/sh

# needed if we are using the scss precompiler
# loads the ruby env so that compressor can find the sass command.
source /opt/elasticbeanstalk/lib/ruby/profile.sh
python manage.py compress &> /tmp/compress-output
