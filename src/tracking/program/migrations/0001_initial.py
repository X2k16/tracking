# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='名前', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'セッション',
                'verbose_name': 'セッション',
                'ordering': ('timespan', 'venue'),
            },
        ),
        migrations.CreateModel(
            name='ProgramAttendance',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('is_enabled', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
            ],
            options={
                'verbose_name_plural': 'セッション',
                'verbose_name': 'セッション',
                'ordering': ('timespan',),
            },
        ),
        migrations.CreateModel(
            name='Timespan',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_at', models.TimeField(verbose_name='開始時間')),
                ('end_at', models.TimeField(verbose_name='終了時間')),
                ('name', models.CharField(verbose_name='時間帯名', max_length=100)),
            ],
            options={
                'verbose_name_plural': '時間帯',
                'verbose_name': '時間帯',
                'ordering': ('start_at',),
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('ordering', models.IntegerField(default=0, verbose_name='表示順')),
                ('name', models.CharField(verbose_name='名前', max_length=100)),
            ],
            options={
                'verbose_name_plural': '会場',
                'verbose_name': '会場',
                'ordering': ('ordering', 'id'),
            },
        ),
    ]
