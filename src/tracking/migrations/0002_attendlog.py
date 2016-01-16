# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendLog',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('date', models.DateTimeField(verbose_name='確認日時')),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
                ('participant', models.ForeignKey(to='tracking.Participant')),
                ('program', models.ForeignKey(to='program.Program')),
                ('venue', models.ForeignKey(to='program.Venue')),
            ],
            options={
                'verbose_name_plural': '入場履歴',
                'verbose_name': '入場履歴',
                'ordering': ('date',),
            },
        ),
    ]
