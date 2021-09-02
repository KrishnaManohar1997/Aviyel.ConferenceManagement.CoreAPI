from conference.models import Conference
from django.core.exceptions import ValidationError

from conference.repositories import ConferenceRepository


class ConferenceService:
    conference_repo = ConferenceRepository()

    def get_conferences(self):
        return self.conference_repo.get_conferences()

    def get_conferences_by_owner_id(self, owner_user_id):
        return self.conference_repo.get_conferences_by_owner_id(owner_user_id)

    def increment_conference_talks_count(self, conference: Conference):
        self.conference_repo.increment_conference_talks_count(conference)

    def get_conference_by_id_or_none(self, conference_id):
        try:
            return self.conference_repo.get_conference_by_id(conference_id)
        except Conference.DoesNotExist:
            return None

    def is_title_available(self, title):
        return self.conference_repo.is_title_available(title)
