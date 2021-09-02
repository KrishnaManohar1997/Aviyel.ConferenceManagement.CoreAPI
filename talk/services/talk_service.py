from talk.repositories import TalkRepository


class TalkService:
    talk_repo = TalkRepository()

    def get_talks_by_conference_id(self, conference_id):
        return self.talk_repo.get_talks_by_conference_id(conference_id)
