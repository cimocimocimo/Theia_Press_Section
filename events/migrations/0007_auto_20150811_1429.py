# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_event_location_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='video_still',
            new_name='main_image',
        ),
    ]
