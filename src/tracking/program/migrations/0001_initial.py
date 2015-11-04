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
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(verbose_name='名前', max_length=100)),
            ],
            options={
                'ordering': ('timespan', 'venue'),
                'verbose_name': 'セッション',
                'verbose_name_plural': 'セッション',
            },
        ),
        migrations.CreateModel(
            name='Timespan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('start_at', models.TimeField(verbose_name='開始時間')),
                ('end_at', models.TimeField(verbose_name='終了時間')),
                ('name', models.CharField(verbose_name='時間帯名', max_length=100)),
            ],
            options={
                'ordering': ('start_at',),
                'verbose_name': '時間帯',
                'verbose_name_plural': '時間帯',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ordering', models.IntegerField(verbose_name='表示順', default=0)),
                ('name', models.CharField(verbose_name='名前', max_length=100)),
            ],
            options={
                'ordering': ('ordering', 'id'),
                'verbose_name': '会場',
                'verbose_name_plural': '会場',
            },
        ),
        migrations.AddField(
            model_name='program',
            name='timespan',
            field=models.ForeignKey(to='program.Timespan'),
        ),
        migrations.AddField(
            model_name='program',
            name='venue',
            field=models.ForeignKey(to='program.Venue'),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('timespan', 'venue')]),
        ),
    ]
