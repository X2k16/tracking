# coding=utf-8
from django.core.management.base import BaseCommand
from tracking.models import Participant
from tracking.enquete.models import ProgramEnquete


class Command(BaseCommand):

    args = "type"

    def handle(self, *args, **options):
        if args[0] == "participant":
            self.do_participant()

        if args[0] == "programenquete":
            self.do_programenquete()

    def do_participant(self):
        fields = ["id", "job_type", "sex", "age", "times", "how_to_know", "good_program", "dpz", "kikaku", "access", "equipment", "will_attend", "comment"]
        print(",".join(fields))
        for p in Participant.objects.exclude(sex=""):
            cols = []
            for f in fields:
                if hasattr(p, "get_{0}_display".format(f)):
                    data = getattr(p, "get_{0}_display".format(f))()
                else:
                    data = getattr(p, f)

                if "\n" in str(data):
                    data = '"{0}"'.format(data)

                if data is None:
                    data = ""

                cols.append(str(data))

            print(",".join(cols))

    def do_programenquete(self):
        fields = ["id", "participant_id", "program_id", "program", "is_good", "comment"]
        print(",".join(fields))
        for p in ProgramEnquete.objects.order_by("id"):
            cols = []
            for f in fields:
                if hasattr(p, "get_{0}_display".format(f)):
                    data = getattr(p, "get_{0}_display".format(f))()
                else:
                    data = getattr(p, f)

                if data is None:
                    data = ""

                if "\n" in str(data):
                    data = '"{0}"'.format(data)

                cols.append(str(data))

            print(",".join(cols))
