# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_participant_bonus_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, verbose_name='名前', blank=True)),
                ('hartbeat_at', models.DateTimeField(null=True, verbose_name='最終接続時刻', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
            ],
            options={
                'ordering': ('name', 'id'),
                'verbose_name_plural': '受信機',
                'verbose_name': '受信機',
            },
        ),
        migrations.AddField(
            model_name='attendlog',
            name='client',
            field=models.ForeignKey(null=True, blank=True, to='tracking.Client'),
        ),
    ]
