# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='programattendance',
            name='participant',
            field=models.ForeignKey(to='tracking.Participant'),
        ),
        migrations.AddField(
            model_name='programattendance',
            name='program',
            field=models.ForeignKey(to='program.Program'),
        ),
        migrations.AddField(
            model_name='programattendance',
            name='timespan',
            field=models.ForeignKey(to='program.Timespan'),
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
            name='programattendance',
            unique_together=set([('participant', 'program')]),
        ),
        migrations.AlterUniqueTogether(
            name='program',
            unique_together=set([('timespan', 'venue')]),
        ),
    ]
