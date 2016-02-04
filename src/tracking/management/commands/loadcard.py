# coding=utf-8
from django.core.management.base import BaseCommand
from tracking.models import Participant
import base64
import hashlib
import uuid


class Command(BaseCommand):

    args = 'csvfilename'

    def handle(self, *args, **options):
        filename = args[0]

        with open(filename) as f:
            for line in f.readlines():
                line = line.strip().split(",")
                id = int(line[0])
                card_id = line[1]
                Participant.objects.filter(id=id).update(card_id=card_id)
