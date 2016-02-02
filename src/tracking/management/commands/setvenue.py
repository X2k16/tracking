# coding=utf-8
import datetime
from django.core.management.base import BaseCommand
from tracking.program.models import Venue
from tracking.models import Terminal


class Command(BaseCommand):
    args = "current new"

    def handle(self, *args, **options):
        # 指定した会場の端末を別の会場に変更する
        current = Venue.objects.get(id=args[0])
        new = Venue.objects.get(id=args[1])
        Terminal.objects.filter(venue=current).update(venue=new)
