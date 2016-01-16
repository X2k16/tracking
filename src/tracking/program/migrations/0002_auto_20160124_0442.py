# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20160116_2343'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramAttendance',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('is_enabled', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
                ('participant', models.ForeignKey(to='tracking.Participant')),
                ('program', models.ForeignKey(to='program.Program')),
                ('timespan', models.ForeignKey(to='program.Timespan')),
            ],
            options={
                'verbose_name': 'セッション',
                'ordering': ('timespan',),
                'verbose_name_plural': 'セッション',
            },
        ),
        migrations.AlterUniqueTogether(
            name='programattendance',
            unique_together=set([('participant', 'program')]),
        ),
    ]
