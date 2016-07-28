# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20160728_1151'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questions',
            options={},
        ),
        migrations.RemoveField(
            model_name='questions',
            name='created',
        ),
    ]
