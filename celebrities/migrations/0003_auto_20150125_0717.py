# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0002_auto_20150124_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebrity',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='dress',
            name='main_image',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
