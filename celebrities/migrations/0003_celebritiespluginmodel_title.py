# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0002_celebritiespluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='celebritiespluginmodel',
            name='title',
            field=models.CharField(default=b'Celebrities', max_length=255),
            preserve_default=True,
        ),
    ]
