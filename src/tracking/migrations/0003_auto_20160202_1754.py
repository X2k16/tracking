# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0003_auto_20160128_2118'),
        ('tracking', '0002_auto_20160202_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='good_program',
            field=models.ForeignKey(null=True, blank=True, to='program.Program', verbose_name='最も良かったプログラム'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='access',
            field=models.IntegerField(choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], blank=True, verbose_name='会場アクセスはいかがでしたか？', null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='equipment',
            field=models.IntegerField(choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], blank=True, verbose_name='会場の設備はいかがでしたでしょうか？', null=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='times',
            field=models.IntegerField(choices=[(1, '初めて'), (2, '2回目'), (3, '3回目'), (4, '4回目'), (5, '5回目')], blank=True, verbose_name='参加回数', null=True),
        ),
    ]
