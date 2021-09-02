from talk.serializers import CreateTalkSerializer
from talk.services import TalkService
from common.base_view import BaseView
from conference.services import ConferenceService


class CreateTalkView(BaseView):
    talk_service = TalkService()
    serializer = CreateTalkSerializer
    conference_service = ConferenceService()

    def post(self, request, conference_id):
        conference = self.conference_service.get_conference_by_id_or_none(conference_id)
        if not conference:
            return self.resource_not_found_response("Conference", conference_id)
        request.data["conference"] = conference.id
        talk_create_serializer = self.serializer(data=request.data)
        if not talk_create_serializer.is_valid():
            return self.serializer_error_response(
                "Talk Creation failed", talk_create_serializer.errors
            )
        talk = talk_create_serializer.save()
        self.conference_service.increment_conference_talks_count(conference)
        return self.resource_created_response("Talk", talk.id)
