# coding=utf-8
import datetime
from django.core.management.base import BaseCommand
from tracking.program.models import Program


class Command(BaseCommand):

    def handle(self, *args, **options):
        for program in Program.objects.all():
            title = program.data["title"]
            if program.name != title:
                program.name = title
                program.save()
