# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0003_auto_20160205_0135'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendlog',
            options={'verbose_name_plural': '入場履歴', 'ordering': ('-date',), 'verbose_name': '入場履歴'},
        ),
        migrations.AddField(
            model_name='participant',
            name='dpz',
            field=models.IntegerField(null=True, choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], blank=True, verbose_name='デイリーポータルZのお楽しみコーナーはいかがでしたか？'),
        ),
        migrations.AddField(
            model_name='participant',
            name='kikaku',
            field=models.IntegerField(null=True, choices=[(4, 'とても良かった'), (3, '良かった'), (2, '悪かった'), (1, 'とても悪かった')], blank=True, verbose_name='その他の企画等はいかがでしたか？'),
        ),
        migrations.AlterField(
            model_name='participant',
            name='job_type',
            field=models.CharField(max_length=100, choices=[('SI', 'SIエンジニア'), ('インフラ', 'インフラエンジニア'), ('フロントエンド', 'フロントエンドエンジニア'), ('Web', 'Webエンジニア'), ('デザイナ', 'デザイナー系'), ('運用', 'IT運用/オペレータ'), ('営業', '営業'), ('人事', '人事'), ('広報', '広報/マーケティング'), ('その他', 'その他')], blank=True, verbose_name='職種'),
        ),
    ]
