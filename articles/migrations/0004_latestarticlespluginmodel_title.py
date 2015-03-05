# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20150305_0627'),
    ]

    operations = [
        migrations.AddField(
            model_name='latestarticlespluginmodel',
            name='title',
            field=models.CharField(default=b'Latest Articles', max_length=255),
            preserve_default=True,
        ),
    ]
