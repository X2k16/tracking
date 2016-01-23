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

    # TODO:アンケート項目
    is_good = models.BooleanField("よかった(サンプル)")

    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)
