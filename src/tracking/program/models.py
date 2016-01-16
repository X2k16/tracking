# coding=utf-8
from django.db import models


class Timespan(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "時間帯"
        ordering = ("start_at",)

    start_at = models.TimeField("開始時間")
    end_at = models.TimeField("終了時間")
    name = models.CharField("時間帯名", max_length=100)

    def __str__(self):
        return "[{0}-{1}] {2}".format(self.start_at, self.end_at, self.name)


class Venue(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "会場"
        ordering = ("ordering", "id")

    ordering = models.IntegerField("表示順", default=0)
    name = models.CharField("名前", max_length=100)

    def __str__(self):
        return self.name


class Program(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "セッション"
        ordering = ("timespan", "venue")
        unique_together = (("timespan", "venue"),)

    name = models.CharField("名前", max_length=100)
    timespan = models.ForeignKey(Timespan)
    venue = models.ForeignKey(Venue)

    def __str__(self):
        return self.name
