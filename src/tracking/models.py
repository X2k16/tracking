# coding=utf-8

import uuid

from django.db import models
from django.contrib.auth.models import User


class Participant(User):
    card_id = models.CharField("カードID", max_length=255)
    login_token = models.CharField("ログイントークン", max_length=100, unique=True)

    #　属性情報
    JOB_TYPE_CHOICES = (
        ("Web", "Webエンジニア"),
        ("SI", "SIエンジニア"),
        ("基幹", "基幹エンジニア"),
        ("UI", "UIエンジニア"),
        ("デザイナ", "デザイナー系"),
        ("運用", "IT運用/オペレータ"),
        ("営業", "営業"),
        ("人事", "人事"),
        ("広報", "広報/マーケティング"),
        ("その他", "その他")
    )
    job_type = models.CharField("職種", max_length=100, choices=JOB_TYPE_CHOICES, blank=True)
    SEX_CHOICES = (
        ("男性", "男性"),
        ("女性", "女性")
    )
    sex = models.CharField("性別", max_length=10, choices=SEX_CHOICES, blank=True)
    AGE_CHOICES = (
        ("10", "10代"),
        ("20", "20代"),
        ("30", "30代"),
        ("40", "40代"),
        ("50", "50代"),
        ("60", "60代"),
        ("70+", "それ以上"),
    )
    age = models.CharField("年齢", max_length=10, choices=AGE_CHOICES, blank=True)
    TIMES_CHOICES = (
        (1, "初めて"),
        (2, "2回目"),
        (3, "3回目"),
        (4, "4回目"),
        (5, "5回目"),
    )
    times = models.IntegerField("参加回数", choices=TIMES_CHOICES, blank=True, null=True)
    HOW_TO_KNOW_CHOICES = (
        ("Twitter", "Twitter"),
        ("Facebook", "Facebook"),
        ("Web", "その他Web経由"),
        ("上長", "上長"),
        ("知人", "知人/友人"),
        ("団体", "所属団体/企業から"),
        ("以前から知っていた", "以前から知っていた"),
    )
    how_to_know = models.CharField("CROSSを何で知りましたか？", max_length=50, choices=HOW_TO_KNOW_CHOICES, blank=True)

    # CROSSに関するアンケート
    GOOD_CHOICES = (
        (4, "とても良かった"),
        (3, "良かった"),
        (2, "悪かった"),
        (1, "とても悪かった"),
    )
    access = models.IntegerField("会場アクセスはいかがでしたか？", choices=GOOD_CHOICES, blank=True, null=True)
    equipment = models.IntegerField("会場の設備はいかがでしたでしょうか？", choices=GOOD_CHOICES, blank=True, null=True)
    WILL_ATTEND_CHOICES = (
        ("来場者", "来場者として参加したい"),
        ("登壇者", "登壇者として参加したい"),
        ("スポンサー", "スポンサーとして参加したい"),
        ("不明", "わからない"),
        ("不参加", "参加したくない")
    )
    will_attend = models.CharField("会場の設備はいかがでしたでしょうか？", max_length=20, choices=WILL_ATTEND_CHOICES, blank=True, null=True)
    comment = models.TextField("ご意見・ご感想", blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.login_token:
            self.login_token = str(uuid.uuid4())

    def is_answered(self):
        if self.job_type:
            return True
        return False

    def is_cross_answered(self):
        if self.access:
            return True
        return False


class Terminal(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "NFC端末"
        ordering = ("name", "id")

    mac = models.CharField("MACアドレス", max_length=17, unique=True)
    name = models.CharField("名前", max_length=200, blank=True)
    venue = models.ForeignKey("program.Venue", blank=True, null=True)

    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)

    def __str__(self):
        return "[{0}] {1} @{2}".format(self.mac, self.name, self.venue)


class AttendLog(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "入場履歴"
        ordering = ("date",)

    date = models.DateTimeField("確認日時")
    participant = models.ForeignKey(Participant)
    terminal = models.ForeignKey(Terminal, blank=True, null=True)
    venue = models.ForeignKey("program.Venue", blank=True, null=True)
    timespan = models.ForeignKey("program.Timespan", blank=True, null=True)
    program = models.ForeignKey("program.Program", blank=True, null=True)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)
