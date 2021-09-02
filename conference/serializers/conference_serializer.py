from conference.services import ConferenceService
from conference.models import Conference
from rest_framework import serializers


class CreateConferenceSerializer(serializers.ModelSerializer):
    conference_service = ConferenceService()

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

    def validate_title(self, title):
        if not self.conference_service.is_title_available(title):
            raise serializers.ValidationError(
                {"title": "Title is unavailable, please try with another one"}
            )
        return title

    def validate(self, data):
        # Ensures Start Date is Always less than end Date
        if data["start_date"] > data["end_date"]:
            raise serializers.ValidationError(
                {"end_date": "End Date must occur after start date"}
            )
        return data


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
