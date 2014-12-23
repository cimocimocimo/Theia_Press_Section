# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20141222_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 2, 19, 40, 796114)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=256),
            preserve_default=True,
        ),
    ]
