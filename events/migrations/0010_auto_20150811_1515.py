# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_event_extra_contact_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_date',
        ),
        migrations.AddField(
            model_name='event',
            name='event_date_from',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='event_date_to',
            field=models.DateTimeField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
