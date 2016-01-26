# coding=utf-8

import uuid

from django.db import models
from django.contrib.auth.models import User


class Participant(User):
    card_id = models.CharField("カードID", max_length=255)
    login_token = models.CharField("ログイントークン", max_length=100, unique=True)

    #　属性情報
    JOB_TYPE_CHOICES = (
        ("Web", "Web"),
        ("通信", "通信"),
        ("ほげ", "ほげ"),
        ("fuga", "fuga"),
    )
    job_type = models.CharField("職種", max_length=100, choices=JOB_TYPE_CHOICES, blank=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.login_token:
            self.login_token = str(uuid.uuid4())

    def is_answered(self):
        if self.job_type:
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
