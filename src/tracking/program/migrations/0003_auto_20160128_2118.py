# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
        ('program', '0002_auto_20160126_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='VenueAttendance',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('is_enabled', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('participant', models.ForeignKey(to='tracking.Participant')),
                ('venue', models.ForeignKey(to='program.Venue')),
            ],
            options={
                'verbose_name_plural': '会場参加',
                'verbose_name': '会場参加',
                'ordering': ('created_at',),
            },
        ),
        migrations.AlterModelOptions(
            name='programattendance',
            options={'verbose_name_plural': 'セッション参加', 'verbose_name': 'セッション参加', 'ordering': ('timespan',)},
        ),
        migrations.AlterUniqueTogether(
            name='venueattendance',
            unique_together=set([('participant', 'venue')]),
        ),
    ]
