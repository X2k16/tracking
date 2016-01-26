# coding=utf-8
from django import forms
from tracking.program.models import Program
from tracking.enquete.models import ProgramEnquete
from tracking.models import Participant


class ParticipantForm(forms.ModelForm):

    class Meta:
        model = Participant
        fields = ("last_name", "first_name", "email", "job_type")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True


class ProgramEnqueteForm(forms.ModelForm):
    class Meta:
        model = ProgramEnquete
        exclude = ("participant", "timespan")

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["program"].queryset = Program.objects.filter(
            timespan = self.instance.timespan
        )
