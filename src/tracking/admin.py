# coding=utf-8
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponse
from tracking.models import Participant, AttendLog, Terminal
from tracking.pdf import generate_sherets_pdf


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ("id", "card_id")

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            url(r'^sheet.pdf$', self.admin_site.admin_view(self.sheet_pdf), name='sheet_pdf'),
        ]
        return my_urls + urls

    def sheet_pdf(self, request):
        perticipants = Participant.objects.all().order_by("id")
        response = HttpResponse(content_type="application/pdf")
        return generate_sherets_pdf(perticipants, response)

admin.site.register(Participant, ParticipantAdmin)

class TerminalAdmin(admin.ModelAdmin):
    list_display = ("id", "mac", "name", "venue")
    list_filter = ("venue",)

admin.site.register(Terminal, TerminalAdmin)


class AttendLogAdmin(admin.ModelAdmin):
    list_display = ("id", "terminal", "venue", "program")

admin.site.register(AttendLog, AttendLogAdmin)
