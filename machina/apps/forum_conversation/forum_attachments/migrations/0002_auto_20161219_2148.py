# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-19 21:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_attachments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(upload_to='forum/attachments', verbose_name='File'),
        ),
    ]