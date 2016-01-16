# encoding=utf-8

from django import forms
from tracking.models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ("last_name", "first_name", "email", "job_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True
