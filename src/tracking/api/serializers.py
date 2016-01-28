# coding=utf-8
from rest_framework import serializers
from tracking.program.models import Timespan, Venue, Program, VenueAttendance


class TimespanSerializer(serializers.ModelSerializer):

    class Meta:
        model = Timespan
        fields = ('id', 'name', 'start_at', 'end_at')


class VenueSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venue
        fields = ('id', 'ordering', 'name', 'count')

    count = serializers.SerializerMethodField()

    def get_count(self, obj):
        return VenueAttendance.objects.filter(is_enabled=True, venue=obj).count()


class ProgramSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = (
            'id', 'name', 'timespan', 'venue',
            'title', 'detail', 'owners', 'speakers'
        )

    title = serializers.SerializerMethodField()
    detail = serializers.SerializerMethodField()
    owners = serializers.SerializerMethodField()
    speakers = serializers.SerializerMethodField()

    def get_title(self, obj):
        return obj.data["title"]

    def get_detail(self, obj):
        return obj.data["detail"]

    def get_owners(self, obj):
        return obj.data["owner"]

    def get_speakers(self, obj):
        return obj.data["speaker"]

class AudienceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Program
        fields = (
            'id',
            'program',
            'count'
        )

    id = serializers.SerializerMethodField()
    program = serializers.SerializerMethodField()
    count = serializers.SerializerMethodField()

    def get_id(self, obj):
        return obj["program_id"]
    def get_program(self, obj):
        return obj["program_id"]
    def get_count(self, obj):
        return obj["count"]
