# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='access',
            field=models.IntegerField(verbose_name='会場アクセスはいかがでしたか？', choices=[('4', 'とても良かった'), ('3', '良かった'), ('2', '悪かった'), ('1', 'とても悪かった')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='age',
            field=models.CharField(max_length=10, verbose_name='年齢', choices=[('10', '10代'), ('20', '20代'), ('30', '30代'), ('40', '40代'), ('50', '50代'), ('60', '60代'), ('70+', 'それ以上')], blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='comment',
            field=models.TextField(verbose_name='ご意見・ご感想', blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='equipment',
            field=models.IntegerField(verbose_name='会場の設備はいかがでしたでしょうか？', choices=[('4', 'とても良かった'), ('3', '良かった'), ('2', '悪かった'), ('1', 'とても悪かった')], null=True, blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='how_to_know',
            field=models.CharField(max_length=50, verbose_name='CROSSを何で知りましたか？', choices=[('Twitter', 'Twitter'), ('Facebook', 'Facebook'), ('Web', 'その他Web経由'), ('上長', '上長'), ('知人', '知人/友人'), ('団体', '所属団体/企業から'), ('以前から知っていた', '以前から知っていた')], blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='sex',
            field=models.CharField(max_length=10, verbose_name='性別', choices=[('男性', '男性'), ('女性', '女性')], blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='times',
            field=models.IntegerField(verbose_name='参加回数', null=True, blank=True),
        ),
        migrations.AddField(
            model_name='participant',
            name='will_attend',
            field=models.CharField(max_length=20, verbose_name='会場の設備はいかがでしたでしょうか？', choices=[('来場者', '来場者として参加したい'), ('登壇者', '登壇者として参加したい'), ('スポンサー', 'スポンサーとして参加したい'), ('不明', 'わからない'), ('不参加', '参加したくない')], null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='participant',
            name='job_type',
            field=models.CharField(max_length=100, verbose_name='職種', choices=[('Web', 'Webエンジニア'), ('SI', 'SIエンジニア'), ('基幹', '基幹エンジニア'), ('UI', 'UIエンジニア'), ('デザイナ', 'デザイナー系'), ('運用', 'IT運用/オペレータ'), ('営業', '営業'), ('人事', '人事'), ('広報', '広報/マーケティング'), ('その他', 'その他')], blank=True),
        ),
    ]
