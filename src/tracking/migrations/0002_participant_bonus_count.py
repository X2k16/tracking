# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='bonus_count',
            field=models.IntegerField(default=0, verbose_name='抽選ボーナス', blank=True),
        ),
    ]
