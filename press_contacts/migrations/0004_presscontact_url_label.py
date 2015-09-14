# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_contacts', '0003_auto_20150914_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='presscontact',
            name='url_label',
            field=models.CharField(max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
    ]
