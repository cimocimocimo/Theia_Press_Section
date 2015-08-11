# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_eventspluginmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='address',
            field=models.CharField(default=b'New York, NY', max_length=255),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True, blank=True),
            preserve_default=True,
        ),
    ]
