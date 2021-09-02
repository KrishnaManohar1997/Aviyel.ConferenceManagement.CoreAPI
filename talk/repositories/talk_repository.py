from talk.models import Talk


class TalkRepository:
    def get_talks_by_conference_id(self, conference_id):
        return Talk.objects.filter(conference_id=conference_id)
