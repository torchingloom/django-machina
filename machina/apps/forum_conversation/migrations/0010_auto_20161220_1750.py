# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-20 17:50
from __future__ import unicode_literals

from django.db import migrations, models
import machina.core.validators
import machina.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('forum_conversation', '0009_auto_20160925_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=machina.models.fields.MarkupTextField(no_rendered_field=True, validators=[machina.core.validators.NullableMaxLengthValidator(10000)], verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='subject',
            field=models.CharField(max_length=300, verbose_name='Subject'),
        ),
    ]