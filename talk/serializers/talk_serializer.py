from user.serializers import UserProfileSerializer
from talk.models import Talk
from rest_framework import serializers


class TalkSerializer(serializers.ModelSerializer):
    participants = UserProfileSerializer(read_only=True, many=True)
    speakers = UserProfileSerializer(read_only=True, many=True)

    class Meta:
        model = Talk
        fields = [
            "id",
            "title",
            "description",
            "conference_id",
            "created_by_user",
            "start_date",
            "duration",
            "participants",
            "speakers",
        ]


class CreateTalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Talk
        fields = [
            "title",
            "description",
            "conference",
            "created_by_user",
            "start_date",
            "duration",
        ]
