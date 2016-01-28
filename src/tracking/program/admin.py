# coding=utf-8
from django.contrib import admin
from tracking.program.models import *


class TimespanAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "start_at", "end_at")

admin.site.register(Timespan, TimespanAdmin)


class VenueAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "ordering")

admin.site.register(Venue, VenueAdmin)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("id", "timespan", "venue", "name")
    list_filter = ("timespan", "venue")

admin.site.register(Program, ProgramAdmin)


class VenueAttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "participant", "venue", "is_enabled")
    list_filter = ("venue", "is_enabled")

admin.site.register(VenueAttendance, VenueAttendanceAdmin)


class ProgramAttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "participant", "program", "is_enabled")
    list_filter = ("program__venue", "timespan", "is_enabled")

admin.site.register(ProgramAttendance, ProgramAttendanceAdmin)
