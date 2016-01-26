# coding=utf-8
from rest_framework import serializers
from tracking.models import Participant, AttendLog, Terminal
from tracking.program.models import Program, ProgramAttendance, Timespan


class TouchSerializer(serializers.ModelSerializer):

    class Meta:
        model = AttendLog
        fields = ('id', 'date', 'card_id', 'participant', 'mac', 'program', 'created_at', 'updated_at')
        read_only_fields = ('id', 'participant', 'program', 'created_at', 'updated_at')

    card_id = serializers.CharField(write_only=True)
    mac = serializers.CharField(write_only=True)

    def validate_card_id(self, value):
        try:
            self._participant = Participant.objects.get(card_id=value.lower())
        except Participant.DoesNotExist:
            self._participant = None
            raise serializers.ValidationError("NOT_FOUND")
        return value


    def validate_mac(self, value):
        try:
            self._terminal = Terminal.objects.get(mac=value)
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

        # Timespanの取得
        try:
            t = validated_data["date"].time()
            validated_data["timespan"] = Timespan.objects.get(start_at__lte=t, end_at__gte=t)
        except Timespan.DoesNotExist:
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
        return instance
