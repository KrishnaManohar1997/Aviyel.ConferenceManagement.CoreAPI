from conference.models import Conference
from rest_framework import serializers


class CreateConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = [
            "title",
            "description",
            "start_date",
            "end_date",
            "banner_url",
            "created_by_user",
        ]


class ConferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conference
        fields = [
            "id",
            "title",
            "description",
            "start_date",
            "end_date",
            "banner_url",
            "created_by_user",
            "talks_count",
        ]
