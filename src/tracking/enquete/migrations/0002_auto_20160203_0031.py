# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('program', '0001_initial'),
        ('tracking', '0001_initial'),
        ('enquete', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programenquete',
            name='participant',
            field=models.ForeignKey(to='tracking.Participant'),
        ),
        migrations.AddField(
            model_name='programenquete',
            name='program',
            field=models.ForeignKey(verbose_name='参加プログラム', to='program.Program'),
        ),
        migrations.AddField(
            model_name='programenquete',
            name='timespan',
            field=models.ForeignKey(to='program.Timespan'),
        ),
        migrations.AlterUniqueTogether(
            name='programenquete',
            unique_together=set([('participant', 'timespan')]),
        ),
    ]
