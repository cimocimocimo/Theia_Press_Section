# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_eventspluginmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventspluginmodel',
            name='title',
            field=models.CharField(default=b'Events', max_length=255),
            preserve_default=True,
        ),
    ]
