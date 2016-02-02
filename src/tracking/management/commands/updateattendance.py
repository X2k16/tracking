# coding=utf-8
import datetime
from django.core.management.base import BaseCommand
from tracking.program.models import Timespan, Program, VenueAttendance, ProgramAttendance


class Command(BaseCommand):

    def handle(self, *args, **options):
        # 現時刻で所属している会場のプログラムに参加する
        timespan = Timespan.objects.now()
        for venue_attendance in VenueAttendance.objects.filter(is_enabled=True):
            try:
                program = Program.objects.get(timespan=timespan, venue=venue_attendance.venue)

                program_attendance = ProgramAttendance.objects.update_or_create(
                    participant=venue_attendance.participant,
                    timespan=timespan,
                    program=program,
                    defaults={"is_enabled": True}
                )

            except Program.DoesNotExist:
                pass
