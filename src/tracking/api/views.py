# coding=utf-8
from rest_framework import routers, mixins, viewsets

from tracking.program.models import Timespan, Venue, Program
from tracking.api.serializers import TimespanSerializer, VenueSerializer, ProgramSerializer

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
