# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_latestarticlespluginmodel_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='screenshot_2',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
