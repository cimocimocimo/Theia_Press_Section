#!/usr/bin/env python

try: 

    import sys
    # required now to setup the environment
    import django
    django.setup()

    from django.contrib.auth.models import User
    if User.objects.count() == 0:
        admin = User.objects.create_superuser('admin', 'aaron@cimolini.com', 'admin')
        admin.save()

sys.exit()
