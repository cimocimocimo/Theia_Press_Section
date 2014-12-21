# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20141219_0224'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='article',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='published_date',
            field=models.DateField(default=datetime.date(2014, 12, 20)),
            preserve_default=True,
        ),
    ]
