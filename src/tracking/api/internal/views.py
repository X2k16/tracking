# coding=utf-8
from rest_framework import routers, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from tracking.program.models import Timespan, Venue, Program
from tracking.models import Participant, AttendLog, Client
from tracking.api.internal.authentication import InternalAPIKeyAuthentication
from tracking.api.internal.serializers import TouchSerializer, ClientSerializer

router = routers.DefaultRouter()


class ClientViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    viewsets.GenericViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = (InternalAPIKeyAuthentication, )
    permission_classes = (IsAuthenticated,)

router.register("clients", ClientViewSet)


class TouchViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):

    queryset = AttendLog.objects.all()
    serializer_class = TouchSerializer
    authentication_classes = (InternalAPIKeyAuthentication, )
    permission_classes = (IsAuthenticated,)

router.register("touches", TouchViewSet)
