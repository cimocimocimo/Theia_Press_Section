# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0017_event_all_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='by_appointment_only',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='store_hours_closing',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='store_hours_opening',
            field=models.TimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
