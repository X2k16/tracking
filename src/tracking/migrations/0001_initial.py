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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='確認日時')),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
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
                ('user_ptr', models.OneToOneField(serialize=False, primary_key=True, to=settings.AUTH_USER_MODEL, parent_link=True, auto_created=True)),
                ('card_id', models.CharField(verbose_name='カードID', max_length=255)),
                ('login_token', models.CharField(verbose_name='ログイントークン', unique=True, max_length=100)),
                ('job_type', models.CharField(choices=[('Web', 'Webエンジニア'), ('SI', 'SIエンジニア'), ('基幹', '基幹エンジニア'), ('UI', 'UIエンジニア'), ('デザイナ', 'デザイナー系'), ('運用', 'IT運用/オペレータ'), ('営業', '営業'), ('人事', '人事'), ('広報', '広報/マーケティング'), ('その他', 'その他')], verbose_name='職種', blank=True, max_length=100)),
                ('sex', models.CharField(choices=[('男性', '男性'), ('女性', '女性')], verbose_name='性別', blank=True, max_length=10)),
                ('age', models.CharField(choices=[('10', '10代'), ('20', '20代'), ('30', '30代'), ('40', '40代'), ('50', '50代'), ('60', '60代'), ('70+', 'それ以上')], verbose_name='年齢', blank=True, max_length=10)),
                ('times', models.IntegerField(choices=[(1, '初めて'), (2, '2回目'), (3, '3回目'), (4, '4回目'), (5, '5回目')], verbose_name='参加回数', blank=True, null=True)),
                ('how_to_know', models.CharField(choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Web', 'その他Web経由'), ('上長', '上長'), ('知人', '知人/友人'), ('団体', '所属団体/企業から'), ('以前から知っていた', '以前から知っていた')], verbose_name='CROSSを何で知りましたか？', blank=True, max_length=50)),
                ('access', models.IntegerField(choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], verbose_name='会場アクセスはいかがでしたか？', blank=True, null=True)),
                ('equipment', models.IntegerField(choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], verbose_name='会場の設備はいかがでしたでしょうか？', blank=True, null=True)),
                ('will_attend', models.CharField(choices=[('来場者', '来場者として参加したい'), ('登壇者', '登壇者として参加したい'), ('スポンサー', 'スポンサーとして参加したい'), ('不明', 'わからない'), ('不参加', '参加したくない')], verbose_name='会場の設備はいかがでしたでしょうか？', blank=True, max_length=20, null=True)),
                ('comment', models.TextField(verbose_name='ご意見・ご感想', blank=True)),
                ('good_program', models.ForeignKey(blank=True, verbose_name='最も良かったプログラム', null=True, to='program.Program')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('mac', models.CharField(verbose_name='MACアドレス', unique=True, max_length=17)),
                ('name', models.CharField(verbose_name='名前', blank=True, max_length=200)),
                ('created_at', models.DateTimeField(verbose_name='登録日時', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='最終更新日時', auto_now=True)),
                ('venue', models.ForeignKey(blank=True, null=True, to='program.Venue')),
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
