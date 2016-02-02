# coding=utf-8

from django.db import models

"""
class ParticipantEnquete(models.Model):
    "属性情報"
    pass
"""


class ProgramEnquete(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "セッションアンケート"
        ordering = ("-id",)
        unique_together = ("participant", "timespan")

    participant = models.ForeignKey("tracking.Participant")
    timespan = models.ForeignKey("program.Timespan")
    program = models.ForeignKey("program.Program")

    # アンケート項目
    GOOD_CHOICES = (
        ("4", "とても良かった"),
        ("3", "良かった"),
        ("2", "悪かった"),
        ("1", "とても悪かった"),
    )
    is_good = models.IntegerField("このプログラムは良かったですか？", choices=GOOD_CHOICES)
    comment = models.TextField("ご意見・ご感想", blank=True)

    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)
