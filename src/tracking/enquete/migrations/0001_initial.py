# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramEnquete',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('is_good', models.IntegerField(choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], verbose_name='このプログラムは良かったですか？')),
                ('comment', models.TextField(verbose_name='ご意見・ご感想', blank=True)),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'セッションアンケート',
                'verbose_name': 'セッションアンケート',
                'ordering': ('-id',),
            },
        ),
    ]
