# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0020_auto_20150830_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='store_hours_closing',
        ),
        migrations.RemoveField(
            model_name='event',
            name='store_hours_opening',
        ),
    ]
