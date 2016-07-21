# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Que_ans_list',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default=b'', max_length=100, blank=True)),
                ('usn', models.CharField(default=b'', max_length=100, blank=True)),
                ('question_list', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=b'', blank=True), size=None)),
                ('answer_list', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=b'', blank=True), size=None)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
