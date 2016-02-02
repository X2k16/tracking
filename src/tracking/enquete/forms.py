# coding=utf-8
from django import forms
from tracking.program.models import Program
from tracking.enquete.models import ProgramEnquete
from tracking.models import Participant
from tracking.forms import BootstrapMixins


class ParticipantForm(BootstrapMixins, forms.ModelForm):

    class Meta:
        model = Participant
        fields = (
            "sex", "age",
            "job_type", "times", "how_to_know"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not name == "comment":
                field.required = True


class CrossEnqueteForm(BootstrapMixins, forms.ModelForm):

    class Meta:
        model = Participant
        fields = (
            "good_program", "access", "equipment", "will_attend", "comment"
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if not name == "comment":
                field.required = True

        self.fields["good_program"].queryset = Program.objects.filter(
            programattendance__participant=self.instance.participant
        ).order_by("timespan", "venue")


class ProgramEnqueteForm(BootstrapMixins, forms.ModelForm):

    class Meta:
        model = ProgramEnquete
        exclude = ("participant", "timespan")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if not name == "comment":
                field.required = True

        self.fields["program"].queryset = Program.objects.filter(
            timespan=self.instance.timespan,
            programattendance__participant=self.instance.participant
        ).order_by("venue")
