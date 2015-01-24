# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebrity',
            name='main_image',
        ),
        migrations.RemoveField(
            model_name='dress',
            name='main_image',
        ),
    ]
