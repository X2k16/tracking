# encoding=utf-8
import random
from django.db import models
from tracking.models import Participant


class LotteryTicketManager(models.Manager):

    def refresh(self):
        """抽選券の再生成"""
        self.get_queryset().delete()
        for participant in Participant.objects.all():
            count = participant.lottery_count
            if count:
                self.bulk_create([LotteryTicket(participant=participant) for i in range(count)])


class LotteryTicket(models.Model):

    class Meta:
        verbose_name = verbose_name_plural = "抽選券"
        ordering = ("-ordering", )

    participant = models.ForeignKey("tracking.Participant")
    ordering = models.FloatField("乱数", default=lambda: random.uniform(0, 1000))

    objects = LotteryTicketManager()

    def __str__(self):
        return "{0} {1}".format(self.participant, self.ordering)
