# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20150813_1413'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='datetime_from',
            new_name='from_datetime',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='datetime_to',
            new_name='to_datetime',
        ),
    ]
