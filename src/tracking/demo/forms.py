# coding=utf-8

import datetime
from django import forms

from tracking.program.models import Venue
from tracking.models import AttendLog


class TouchForm(forms.Form):
    time = forms.TimeField(label="時刻")
    venue = forms.ModelChoiceField(label="会場", queryset=Venue.objects.all())

    def __init__(self, *args, **kwargs):
        self.participant = kwargs.pop("participant")
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        date = datetime.datetime.combine(datetime.date.today(), self.cleaned_data["time"])
        attend_log = AttendLog(participant=self.participant, date=date)
        if commit:
            attend_log.save()
        return attend_log
