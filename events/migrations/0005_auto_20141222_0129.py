# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_auto_20141222_0100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 1, 29, 15, 103063)),
            preserve_default=True,
        ),
    ]
