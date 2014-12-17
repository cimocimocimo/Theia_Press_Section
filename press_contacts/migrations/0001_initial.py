# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PressContact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('descriptive_text', models.CharField(max_length=2048)),
                ('name', models.CharField(max_length=256)),
                ('address', models.CharField(max_length=512)),
                ('email', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
