# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Multi_choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('question_id', models.CharField(default=b'', max_length=100, blank=True)),
                ('options', django.contrib.postgres.fields.ArrayField(base_field=models.TextField(default=b'', blank=True), size=None)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
