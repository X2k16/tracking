# coding=utf-8
from django.db import models
from rest_framework import routers, mixins, viewsets

from tracking.program.models import Timespan, Venue, Program, ProgramAttendance
from tracking.api.serializers import TimespanSerializer, VenueSerializer, ProgramSerializer, AudienceSerializer

router = routers.DefaultRouter()


class TimeSpanViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Timespan.objects.all()
    serializer_class = TimespanSerializer

router.register("timespans", TimeSpanViewSet)


class VenueViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer

router.register("venues", VenueViewSet)


class ProgramViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

router.register("programs", ProgramViewSet)


class AudienceViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = ProgramAttendance.objects.filter(is_enabled=True).values("program_id").annotate(count=models.Count("id"))
    serializer_class = AudienceSerializer

router.register("audiences", AudienceViewSet, "audiences")
