from talk.models import Talk


class TalkRepository:
    def get_talks_by_conference_id(self, conference_id):
        return Talk.objects.filter(conference_id=conference_id)

    def get_talk_by_conference_and_talk_id(self, conference_id, talk_id):
        return Talk.objects.get(conference_id=conference_id, id=talk_id)

    def __is_speaker_or_participant_eligible(self, talk, user):
        return (
            not talk.participants.filter(id=user.id).exists()
            and not talk.speakers.filter(id=user.id).exists()
        )

    def add_participant(self, talk, participant):
        if self.__is_speaker_or_participant_eligible(talk, participant):
            talk.participants.add(participant)
            talk.save()

    def add_speaker(self, talk, speaker):
        if self.__is_speaker_or_participant_eligible(talk, speaker):
            talk.speakers.add(speaker)
            talk.save()
