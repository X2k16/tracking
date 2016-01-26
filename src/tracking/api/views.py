# coding=utf-8
from django.db import models
from django.core.cache import cache
from django.conf import settings
from rest_framework import routers, mixins, viewsets
from rest_framework.response import Response

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

    def list(self, *args, **kwargs):
        data = cache.get("ProgList", None)
        if data:
            response = Response(data)
        else:
            response = super().list(*args, **kwargs)
            cache.set("ProgList", response.data, settings.PROGRAM_CACHE_TIME)
        return response

router.register("programs", ProgramViewSet)


class AudienceViewSet(mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    queryset = ProgramAttendance.objects.filter(is_enabled=True).values("program_id").annotate(count=models.Count("id"))
    serializer_class = AudienceSerializer

router.register("audiences", AudienceViewSet, "audiences")
