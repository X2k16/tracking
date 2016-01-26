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
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_good', models.BooleanField(verbose_name='よかった(サンプル)')),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
            ],
            options={
                'verbose_name': 'セッションアンケート',
                'ordering': ('-id',),
                'verbose_name_plural': 'セッションアンケート',
            },
        ),
    ]
