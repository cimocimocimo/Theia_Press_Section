# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 07:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    replaces = [(b'gallery', '0001_initial'), (b'gallery', '0002_gallerypluginmodel'), (b'gallery', '0003_auto_20160716_2056')]

    initial = True

    dependencies = [
        ('cms', '0003_auto_20140926_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to=b'')),
                ('link_text', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Image File',
                'verbose_name_plural': 'Image Files',
            },
        ),
        migrations.CreateModel(
            name='PressImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'')),
                ('caption', models.CharField(blank=True, max_length=255, null=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Press Image',
                'verbose_name_plural': 'Press Images',
            },
        ),
        migrations.AddField(
            model_name='imagefile',
            name='press_image',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gallery.PressImage'),
        ),
        migrations.CreateModel(
            name='GalleryPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='gallery_gallerypluginmodel', serialize=False, to='cms.CMSPlugin')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plugins', to='gallery.Gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]