# coding=utf-8
from django import forms
from tracking.program.models import Program
from tracking.enquete.models import ProgramEnquete

class ProgramEnqueteForm(forms.ModelForm):
    class Meta:
        model = ProgramEnquete
        exclude = ("participant", "timespan")

    def __init__(self,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.fields["program"].queryset = Program.objects.filter(
            timespan = self.instance.timespan
        )
