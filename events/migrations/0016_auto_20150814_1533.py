# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_eventconfig'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EventConfig',
            new_name='EventsConfig',
        ),
    ]
