# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('que_ans_list', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='que_ans_list',
            old_name='name',
            new_name='email',
        ),
        migrations.AddField(
            model_name='que_ans_list',
            name='firstname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='que_ans_list',
            name='lastname',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
        migrations.AddField(
            model_name='que_ans_list',
            name='phone',
            field=models.CharField(default=b'', max_length=100, blank=True),
        ),
    ]
