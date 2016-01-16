# coding=utf-8
from rest_framework import serializers
from tracking.program.models import Timespan, Venue, Program


class TimespanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timespan
        fields = ('id', 'name', 'start_at', 'end_at')


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('id', 'ordering', 'name')


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = ('id', 'name', 'timespan', 'venue')
