# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20150125_0742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='screenshot',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
