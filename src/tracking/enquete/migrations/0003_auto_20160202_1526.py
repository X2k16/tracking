# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enquete', '0002_auto_20160126_2357'),
    ]

    operations = [
        migrations.AddField(
            model_name='programenquete',
            name='comment',
            field=models.TextField(verbose_name='ご意見・ご感想', blank=True),
        ),
        migrations.AlterField(
            model_name='programenquete',
            name='is_good',
            field=models.IntegerField(verbose_name='このプログラムは良かったですか？', choices=[('4', 'とても良かった'), ('3', '良かった'), ('2', '悪かった'), ('1', 'とても悪かった')]),
        ),
    ]
