# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_video_still'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='video_still',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True),
            preserve_default=True,
        ),
    ]
