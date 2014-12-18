# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_items', '0002_auto_20141217_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='pressitem',
            name='slug',
            field=models.SlugField(default='hello-world', max_length=256),
            preserve_default=False,
        ),
    ]
