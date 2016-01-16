# coding=utf-8
from rest_framework import routers, mixins, viewsets

from tracking.program.models import Timespan, Venue, Program
from tracking.models import Participant, AttendLog

from tracking.api.internal.serializers import TouchSerializer

router = routers.DefaultRouter()


class TouchViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = AttendLog.objects.all()
    serializer_class = TouchSerializer

router.register("touches", TouchViewSet)
