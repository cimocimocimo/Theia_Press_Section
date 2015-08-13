# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20150813_1248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date_from',
            new_name='datetime_from',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event_date_to',
            new_name='datetime_to',
        ),
    ]
