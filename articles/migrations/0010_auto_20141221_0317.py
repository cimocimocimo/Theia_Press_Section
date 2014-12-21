# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0001_initial'),
        ('articles', '0009_auto_20141221_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='screenshot',
            field=filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 21, 3, 17, 41, 247041)),
            preserve_default=True,
        ),
    ]
