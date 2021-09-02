from user.services import UserService
from talk.serializers import CreateTalkSerializer
from talk.services import TalkService
from common.base_view import BaseView
from conference.services import ConferenceService


class RemoveSpeakerParticipantsView(BaseView):
    talk_service = TalkService()
    serializer = CreateTalkSerializer
    conference_service = ConferenceService()
    user_service = UserService()

    def delete(self, request, conference_id, talk_id):
        talk = self.talk_service.get_talk_by_conference_and_talk_id(
            conference_id, talk_id
        )
        if not talk:
            return self.resource_not_found_response("Talk", talk_id)

        participant_username = request.data.get("participant", None)
        speaker_username = request.data.get("speaker", None)

        if participant_username:
            participant = self.user_service.get_user_by_username(participant_username)
            if participant:
                self.talk_service.remove_participant(talk, participant)

        if speaker_username:
            speaker = self.user_service.get_user_by_username(speaker_username)
            if speaker:
                self.talk_service.remove_speaker(talk, speaker)
        return self.success_response("Speaker/Participants Removed Successfully")
