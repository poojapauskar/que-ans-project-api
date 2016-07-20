# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-20 11:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.CharField(blank=True, default=b'', max_length=100)),
                ('answer', models.CharField(blank=True, default=b'', max_length=100)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
