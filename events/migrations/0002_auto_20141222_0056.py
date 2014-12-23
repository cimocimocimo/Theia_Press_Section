# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_date',
            field=models.DateField(default=datetime.date(2014, 12, 22)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 0, 56, 14, 257260)),
            preserve_default=True,
        ),
    ]
