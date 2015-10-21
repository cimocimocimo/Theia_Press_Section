# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='video',
            field=embed_video.fields.EmbedVideoField(default=b'https://vimeo.com/142393949'),
            preserve_default=True,
        ),
    ]
