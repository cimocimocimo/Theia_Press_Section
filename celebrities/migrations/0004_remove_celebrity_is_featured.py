# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0003_celebrity_main_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='celebrity',
            name='is_featured',
        ),
    ]
