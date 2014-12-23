# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('celebrities', '0005_auto_20141222_0100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dress',
            options={'ordering': ('order',), 'verbose_name': 'Dress', 'verbose_name_plural': 'Dresses'},
        ),
        migrations.AddField(
            model_name='dress',
            name='order',
            field=models.PositiveIntegerField(default=1, editable=False, db_index=True),
            preserve_default=False,
        ),
    ]
