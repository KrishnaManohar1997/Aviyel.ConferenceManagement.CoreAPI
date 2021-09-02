from talk.models import Talk
from talk.repositories import TalkRepository


class TalkService:
    talk_repo = TalkRepository()

    def get_talks_by_conference_id(self, conference_id):
        return self.talk_repo.get_talks_by_conference_id(conference_id)

    def get_talk_by_conference_and_talk_id(self, conference_id, talk_id):
        try:
            return self.talk_repo.get_talk_by_conference_and_talk_id(
                conference_id, talk_id
            )
        except Talk.DoesNotExist:
            return None

    def add_participant(self, talk, participant):
        self.talk_repo.add_participant(talk, participant)

    def remove_participant(self, talk, participant):
        self.talk_repo.remove_participant(talk, participant)

    def add_speaker(self, talk, speaker):
        self.talk_repo.add_speaker(talk, speaker)

    def remove_speaker(self, talk, speaker):
        self.talk_repo.remove_speaker(talk, speaker)
