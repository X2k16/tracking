# coding=utf-8
from django.core.management.base import BaseCommand
from tracking.models import Participant
import base64
import hashlib
import uuid


class Command(BaseCommand):

    args = 'startid count'

    def handle(self, *args, **options):
        start = int(args[0])
        end = int(args[1]) + start
        salt = args[2]

        for index in range(start, end):
            token = base64.b64encode(hashlib.sha1("{0}{1}".format(salt, index).encode("ascii")).digest())
            defaults = {
                "login_token": token,
                "username": "user_{0}".format(index),
                "password": "!{0}".format(uuid.uuid4().hex),
                "card_id": "dummy_{0}".format(index)
            }
            participant, created = Participant.objects.get_or_create(id=index, defaults=defaults)
            if not created:
                defaults.pop("card_id")
                participant.__dict__.update(defaults)
                participant.save()
