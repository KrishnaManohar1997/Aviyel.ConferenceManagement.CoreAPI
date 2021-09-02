from common.base_view import BaseView
from talk.serializers import CreateTalkSerializer
from talk.services import TalkService


class UpdateTalkView(BaseView):
    talk_service = TalkService()
    serializer = CreateTalkSerializer

    def put(self, request, conference_id, talk_id):
        talk = self.talk_service.get_talk_by_conference_and_talk_id(
            conference_id, talk_id
        )
        if not talk:
            return self.resource_not_found_response("Talk", talk_id)
        update_talk_serializer = self.serializer(talk, request.data, partial=True)
        if not update_talk_serializer.is_valid():
            return self.serializer_error_response(
                "Updating Talk failed", update_talk_serializer.errors
            )
        talk = update_talk_serializer.save()
        return self.resource_updated_response("Talk", talk.id)
