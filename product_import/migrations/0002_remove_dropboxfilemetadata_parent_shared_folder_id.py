# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-10-25 23:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_import', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dropboxfilemetadata',
            name='parent_shared_folder_id',
        ),
    ]