# coding=utf-8
from django.contrib import admin
from tracking.models import Participant, AttendLog


class ParticipantAdmin(admin.ModelAdmin):
    pass

admin.site.register(Participant, ParticipantAdmin)
