# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file', models.FileField(upload_to=b'')),
                ('link_text', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Image File',
                'verbose_name_plural': 'Image Files',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PressImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=b'')),
                ('caption', models.CharField(max_length=255, null=True, blank=True)),
                ('gallery', models.ForeignKey(to='gallery.Gallery')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
                'verbose_name': 'Press Image',
                'verbose_name_plural': 'Press Images',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='imagefile',
            name='press_image',
            field=models.ForeignKey(to='gallery.PressImage'),
            preserve_default=True,
        ),
    ]
