# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('press_contacts', '0002_auto_20150226_1445'),
        ('events', '0014_auto_20150813_1518'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventsConfig',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contact', models.ForeignKey(blank=True, to='press_contacts.PressContact', null=True)),
            ],
            options={
                'verbose_name': 'Events Configuration',
            },
            bases=(models.Model,),
        ),
    ]
