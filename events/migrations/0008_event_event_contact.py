# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_contacts', '0002_auto_20150226_1445'),
        ('events', '0007_auto_20150811_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='event_contact',
            field=models.ForeignKey(blank=True, to='press_contacts.PressContact', null=True),
            preserve_default=True,
        ),
    ]
