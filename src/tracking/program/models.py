# coding=utf-8
import requests
import datetime

from django.core.cache import cache
from django.conf import settings
from django.db import models


class TimespanManager(models.Manager):

    def now(self, t=None):
        t = t or datetime.datetime.now().time()
        queryset = self.get_queryset()
        try:
            return queryset.filter(start_at__lte=t, end_at__gte=t).order_by("start_at")[0]
        except IndexError:
            raise Timespan.DoesNotExist


class Timespan(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "時間帯"
        ordering = ("start_at",)

    start_at = models.TimeField("開始時間")
    end_at = models.TimeField("終了時間")
    name = models.CharField("時間帯名", max_length=100)

    objects = TimespanManager()

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
        self._data = self.get_programs()[program_id]
        return self._data

    @classmethod
    def get_programs(cls):
        programs = cache.get('programs')
        if not programs:
            response = requests.get(settings.PROGRAM_API)
            programs = {p["id"]: p for p in response.json()["programs"]}
            cache.set("programs", programs, settings.PROGRAM_CACHE_TIME)
        return programs


class VenueAttendance(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "会場参加"
        ordering = ("created_at",)
        unique_together = (("participant", "venue"),)

    participant = models.ForeignKey("tracking.Participant")
    venue = models.ForeignKey("Venue")
    is_enabled = models.BooleanField()

    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)

    def __str__(self):
        return "{0} {1}".format(self.participant, self.venue)


class ProgramAttendance(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "セッション参加"
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
