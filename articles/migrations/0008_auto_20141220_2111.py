# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0007_auto_20141220_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='original_publication_date',
            field=models.DateField(default=datetime.date(2014, 12, 20)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 20, 21, 11, 56, 698082)),
            preserve_default=True,
        ),
    ]
