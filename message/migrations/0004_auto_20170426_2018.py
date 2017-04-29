# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 14:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0003_remove_list_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bubye',
            name='recv',
        ),
        migrations.RemoveField(
            model_name='bubye',
            name='text',
        ),
        migrations.AddField(
            model_name='bubye',
            name='alumini',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='message.List'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bubye',
            name='message',
            field=models.TextField(default='sad', max_length=5000),
            preserve_default=False,
        ),
    ]
