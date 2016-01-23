# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendLog',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(verbose_name='確認日時')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
            ],
            options={
                'verbose_name_plural': '入場履歴',
                'verbose_name': '入場履歴',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('user_ptr', models.OneToOneField(serialize=False, to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True, primary_key=True)),
                ('card_id', models.CharField(verbose_name='カードID', max_length=255)),
                ('login_token', models.CharField(verbose_name='ログイントークン', unique=True, max_length=100)),
                ('job_type', models.CharField(choices=[('Web', 'Web'), ('通信', '通信'), ('ほげ', 'ほげ'), ('fuga', 'fuga')], max_length=100, verbose_name='職種', blank=True)),
            ],
            options={
                'verbose_name_plural': 'users',
                'verbose_name': 'user',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('mac', models.CharField(verbose_name='MACアドレス', unique=True, max_length=17)),
                ('name', models.CharField(max_length=200, verbose_name='名前', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='最終更新日時')),
                ('venue', models.ForeignKey(null=True, to='program.Venue', blank=True)),
            ],
            options={
                'verbose_name_plural': 'NFC端末',
                'verbose_name': 'NFC端末',
                'ordering': ('name', 'id'),
            },
        ),
        migrations.AddField(
            model_name='attendlog',
            name='participant',
            field=models.ForeignKey(to='tracking.Participant'),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='program',
            field=models.ForeignKey(null=True, to='program.Program', blank=True),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='terminal',
            field=models.ForeignKey(null=True, to='tracking.Terminal', blank=True),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='timespan',
            field=models.ForeignKey(null=True, to='program.Timespan', blank=True),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='venue',
            field=models.ForeignKey(null=True, to='program.Venue', blank=True),
        ),
    ]
