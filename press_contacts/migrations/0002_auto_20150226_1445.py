# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presscontact',
            name='address',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
