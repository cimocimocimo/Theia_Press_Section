# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 07:10
from __future__ import unicode_literals

import datetime
from django.utils import timezone

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import location_field.models.plain
import sorl.thumbnail.fields
import tinymce.models


class Migration(migrations.Migration):

    replaces = [(b'events', '0001_initial'), (b'events', '0002_event_excerpt'), (b'events', '0003_eventspluginmodel'), (b'events', '0004_eventspluginmodel_title'), (b'events', '0005_auto_20150811_1307'), (b'events', '0006_event_location_name'), (b'events', '0007_auto_20150811_1429'), (b'events', '0008_event_event_contact'), (b'events', '0009_event_extra_contact_information'), (b'events', '0010_auto_20150811_1515'), (b'events', '0011_auto_20150813_1248'), (b'events', '0012_auto_20150813_1413'), (b'events', '0013_auto_20150813_1418'), (b'events', '0014_auto_20150813_1518'), (b'events', '0015_eventconfig'), (b'events', '0016_auto_20150815_2336'), (b'events', '0017_event_all_day'), (b'events', '0018_auto_20150828_1434'), (b'events', '0019_auto_20150828_1438'), (b'events', '0020_auto_20150830_1817'), (b'events', '0021_auto_20150830_1818'), (b'events', '0022_auto_20160716_2056')]

    initial = True

    dependencies = [
        ('press_contacts', '0002_auto_20150226_1445'),
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=64, unique=True)),
                ('published_date', models.DateTimeField(default=timezone.now)),
                ('main_image', sorl.thumbnail.fields.ImageField(blank=True, null=True, upload_to=b'')),
                ('content', tinymce.models.HTMLField(blank=True, null=True)),
                ('excerpt', models.TextField(blank=True, null=True)),
                ('address', models.TextField(default=b'New York, NY', help_text=b'Used to search Google for the location.')),
                ('location', location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True)),
                ('location_name', models.CharField(blank=True, max_length=255, null=True)),
                ('event_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='press_contacts.PressContact')),
                ('extra_contact_information', models.TextField(blank=True, null=True)),
                ('from_datetime', models.DateTimeField(default=timezone.now)),
                ('to_datetime', models.DateTimeField(default=timezone.now)),
                ('all_day', models.BooleanField(default=True)),
                ('by_appointment_only', models.BooleanField(default=False)),
                ('store_hours_closing', models.TimeField(blank=True, null=True)),
                ('store_hours_opening', models.TimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
            },
        ),
        migrations.CreateModel(
            name='EventsPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='events_eventspluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(default=b'Events', max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='EventsConfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='press_contacts.PressContact')),
            ],
            options={
                'verbose_name': 'Events Configuration',
            },
        ),
        migrations.CreateModel(
            name='EventLocationHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.IntegerField(choices=[(1, b'Monday'), (2, b'Tuesday'), (3, b'Wednesday'), (4, b'Thursday'), (5, b'Friday'), (6, b'Saturday'), (7, b'Sunday')], unique=True)),
                ('from_hour', models.TimeField()),
                ('to_hour', models.TimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='appointment_only_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='event',
            name='store_hours_closing',
        ),
        migrations.RemoveField(
            model_name='event',
            name='store_hours_opening',
        ),
    ]