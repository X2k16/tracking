# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('user_ptr', models.OneToOneField(to=settings.AUTH_USER_MODEL, auto_created=True, parent_link=True, primary_key=True, serialize=False)),
                ('card_id', models.CharField(max_length=255, verbose_name='カードID')),
                ('login_token', models.CharField(unique=True, max_length=100, verbose_name='ログイントークン')),
                ('job_type', models.CharField(blank=True, max_length=100, choices=[('Web', 'Web'), ('通信', '通信'), ('ほげ', 'ほげ'), ('fuga', 'fuga')], verbose_name='職種')),
            ],
            options={
                'verbose_name': 'user',
                'abstract': False,
                'verbose_name_plural': 'users',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
