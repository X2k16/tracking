# coding=utf-8
import datetime
from django.utils import timezone
from rest_framework import serializers
from tracking.models import Participant, AttendLog, Client, Terminal
from tracking.program.models import Program, ProgramAttendance, Timespan, VenueAttendance

class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ('id', 'name', 'hartbeat_at')
        read_only_fields = fields

    def update(self, instance, validated_data):
        instance.hartbeat_at = timezone.now()
        instance.save()
        return instance


class TouchSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendLog
        fields = ('id', 'date', 'card_id', 'client', 'participant', 'mac', 'program', 'created_at', 'updated_at')
        read_only_fields = ('id', 'participant', 'program', 'created_at', 'updated_at')

    card_id = serializers.CharField(write_only=True)
    mac = serializers.CharField(write_only=True)

    def validate_card_id(self, value):
        try:
            self._participant = Participant.objects.get(card_id=value.upper())
        except Participant.DoesNotExist:
            self._participant = None
            raise serializers.ValidationError("NOT_FOUND")
        return value


    def validate_mac(self, value):
        try:
            self._terminal = Terminal.objects.get(mac=value.upper())
        except:
            self._terminal = None
            raise serializers.ValidationError("NOT_FOUND")
        return value

    def create(self, validated_data):
        validated_data.pop("card_id")
        validated_data.pop("mac")
        validated_data["participant"] = self._participant
        validated_data["terminal"] = self._terminal
        validated_data["timespan"] = None
        validated_data["program"] = None


        # 参加会場の保存
        VenueAttendance.objects.filter(participant=validated_data["participant"], is_enabled=True).update(is_enabled=False)
        if self._terminal.venue:
            venue_attendance, created = VenueAttendance.objects.get_or_create(
                participant=validated_data["participant"],
                venue=self._terminal.venue,
                defaults={"is_enabled":True}
            )
            VenueAttendance.objects.filter(id=venue_attendance.id).update(is_enabled=True)


        # Timespanの取得
        try:
            t = (validated_data["date"]+datetime.timedelta(hours=9, minutes=5)).time()
            print(t)
            queryset = Timespan.objects.filter(start_at__lte=t, end_at__gte=t)
            queryset = queryset.order_by("start_at")
            validated_data["timespan"] = queryset[0]
        except IndexError:
            pass
        else:
            # Programの取得
            try:
                t = validated_data["date"].time()
                venue = self._terminal.venue
                if venue:
                    validated_data["program"] = Program.objects.get(timespan=validated_data["timespan"], venue=venue)
            except Program.DoesNotExist:
                pass

        # すべて不参加にしておく
        ProgramAttendance.objects.filter(
            participant=validated_data["participant"],
            timespan=validated_data["timespan"],
        ).update(is_enabled=False)

        if validated_data["program"]:
            # 最新のプログラムを参加にする
            program_attendance, created = ProgramAttendance.objects.get_or_create(
                participant=validated_data["participant"],
                timespan=validated_data["timespan"],
                program=validated_data["program"],
                defaults={"is_enabled":True}
            )
            ProgramAttendance.objects.filter(id=program_attendance.id).update(is_enabled=True)


        instance = AttendLog(**validated_data)
        instance.save()

        if instance.client:
            instance.client.hartbeat_at = timezone.now()
            instance.client.save()

        return instance
