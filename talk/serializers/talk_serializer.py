from talk.models import Talk
from rest_framework import serializers


class TalkSerializer(serializers.ModelSerializer):
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
        ]
