from functools import partial
from conference.serializers.conference_serializer import CreateConferenceSerializer
from conference.services import ConferenceService
from common.base_view import BaseView


class UpdateConferenceView(BaseView):
    conference_service = ConferenceService()
    serializer = CreateConferenceSerializer

    def put(self, request, conference_id):
        conference = self.conference_service.get_conference_by_id_or_none(
            conference_id=conference_id
        )
        if not conference:
            return self.resource_not_found_response("Conference", conference_id)
        conference_create_serializer = self.serializer(
            instance=conference, data=request.data
        )
        if not conference_create_serializer.is_valid():
            return self.serializer_error_response(
                "Updating Conference failed", conference_create_serializer.errors
            )
        conference = conference_create_serializer.save()
        return self.resource_updated_response("Conference", conference.id)
