# coding=utf-8
from rest_framework import serializers
from tracking.models import Participant, AttendLog
from tracking.program.models import Program


class TouchSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendLog
        fields = ('id', 'date', 'card_id', 'participant', 'venue', 'program', 'created_at', 'updated_at')
        read_only_fields = ('id', 'participant', 'program', 'created_at', 'updated_at')

    card_id = serializers.CharField(write_only=True)

    def validate_card_id(self, value):
        try:
            self._participant = Participant.objects.get(card_id=value)
        except Participant.DoesNotExist:
            self._participant = None
            raise serializers.ValidationError("NOT_FOUND")
        return value

    def create(self, validated_data):
        validated_data.pop("card_id")
        validated_data["participant"] = self._participant

        # Programの取得
        try:
            t = validated_data["date"].time()
            venue = validated_data["venue"]
            validated_data["program"] = Program.objects.get(timespan__start_at__lte=t, timespan__end_at__gte=t, venue=venue)
            print(validated_data["program"])
        except Program.DoesNotExist:
            pass

        instance = AttendLog(**validated_data)
        instance.save()
        return instance
