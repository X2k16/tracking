# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_attendlog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendlog',
            name='program',
            field=models.ForeignKey(to='program.Program', null=True, blank=True),
        ),
    ]
