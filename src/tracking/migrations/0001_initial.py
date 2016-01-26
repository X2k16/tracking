# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.auth.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('program', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendLog',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name='確認日時')),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
            ],
            options={
                'verbose_name': '入場履歴',
                'verbose_name_plural': '入場履歴',
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('user_ptr', models.OneToOneField(primary_key=True, auto_created=True, to=settings.AUTH_USER_MODEL, parent_link=True, serialize=False)),
                ('card_id', models.CharField(verbose_name='カードID', max_length=255)),
                ('login_token', models.CharField(verbose_name='ログイントークン', unique=True, max_length=100)),
                ('job_type', models.CharField(verbose_name='職種', blank=True, choices=[('Web', 'Web'), ('通信', '通信'), ('ほげ', 'ほげ'), ('fuga', 'fuga')], max_length=100)),
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
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('mac', models.CharField(verbose_name='MACアドレス', unique=True, max_length=17)),
                ('name', models.CharField(verbose_name='名前', blank=True, max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
                ('venue', models.ForeignKey(blank=True, null=True, to='program.Venue')),
            ],
            options={
                'verbose_name': 'NFC端末',
                'verbose_name_plural': 'NFC端末',
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
            field=models.ForeignKey(blank=True, null=True, to='program.Program'),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='terminal',
            field=models.ForeignKey(blank=True, null=True, to='tracking.Terminal'),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='timespan',
            field=models.ForeignKey(blank=True, null=True, to='program.Timespan'),
        ),
        migrations.AddField(
            model_name='attendlog',
            name='venue',
            field=models.ForeignKey(blank=True, null=True, to='program.Venue'),
        ),
    ]
