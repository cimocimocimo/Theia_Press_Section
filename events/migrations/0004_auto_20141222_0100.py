# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20141222_0056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 22, 1, 0, 24, 522499)),
            preserve_default=True,
        ),
    ]
