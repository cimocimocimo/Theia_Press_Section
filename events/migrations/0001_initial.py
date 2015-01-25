# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import datetime
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True, max_length=64)),
                ('event_date', models.DateField(default=datetime.date.today)),
                ('published_date', models.DateTimeField(default=datetime.datetime.now)),
                ('video_still', sorl.thumbnail.fields.ImageField(null=True, upload_to=b'', blank=True)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'event_content', editable=False, to='cms.Placeholder', null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
            bases=(models.Model,),
        ),
    ]
