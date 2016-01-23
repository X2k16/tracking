# coding=utf-8
import requests

from django.core.cache import cache
from django.conf import settings
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


    @property
    def data(self):
        if getattr(self, "_data", None):
            return self._data

        venues = {
            1: "x",
            2: "a",
            3: "b",
            4: "c",
            5: "d",
            6: "e"
        }
        program_id = "{0}{1}".format(venues[self.venue_id], self.timespan_id)
        cache_key = "program_{0}".format(program_id)
        data = cache.get(cache_key)
        if not data:
            data = self.get_programs()[program_id]
            cache.set(cache_key, data, 30)
        self._data = data
        return data

    @classmethod
    def get_programs(cls):
        programs = cache.get('programs')
        if not programs:
            response = requests.get(settings.PROGRAM_API)
            programs = {p["id"]: p for p in response.json()["programs"]}
            cache.set("programs", programs, 30)
        return programs


class ProgramAttendance(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "セッション"
        ordering = ("timespan",)
        unique_together = (("participant", "program"),)

    participant = models.ForeignKey("tracking.Participant")
    timespan = models.ForeignKey(Timespan)
    program = models.ForeignKey(Program)
    is_enabled = models.BooleanField()

    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.participant, self.program)
