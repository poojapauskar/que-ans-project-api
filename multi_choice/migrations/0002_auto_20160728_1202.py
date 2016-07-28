# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('multi_choice', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multi_choice',
            options={},
        ),
        migrations.RemoveField(
            model_name='multi_choice',
            name='created',
        ),
    ]
