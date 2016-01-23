# coding=utf-8
from django.contrib import admin
from tracking.models import Participant, AttendLog, Terminal


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("id", "card_id")

admin.site.register(Participant, ParticipantAdmin)

class TerminalAdmin(admin.ModelAdmin):
    list_display = ("id", "mac", "name", "venue")
    list_filter = ("venue",)

admin.site.register(Terminal, TerminalAdmin)


class AttendLogAdmin(admin.ModelAdmin):
    list_display = ("id", "terminal", "venue", "program")

admin.site.register(AttendLog, AttendLogAdmin)
