# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_event_event_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='extra_contact_information',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
