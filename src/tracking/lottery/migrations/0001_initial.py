# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_participant_bonus_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='LotteryTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('ordering', models.FloatField(verbose_name='乱数')),
                ('participant', models.ForeignKey(to='tracking.Participant')),
            ],
            options={
                'ordering': ('-ordering',),
                'verbose_name_plural': '抽選券',
                'verbose_name': '抽選券',
            },
        ),
    ]
