#!/usr/bin/env python

from django.contrib.auth.models import User
if User.objects.count() == 0:
    admin = User.objects.create_superuser('admin', 'aaron@cimolini.com', 'admin')
    admin.save()
