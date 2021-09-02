from django.db.models import F

from conference.models import Conference


class ConferenceRepository:
    def get_conference_by_id(self, conference_id):
        return Conference.objects.get(id=conference_id)

    def get_conferences(self):
        return Conference.objects.all()

    def get_conferences_by_owner_id(self, owner_user_id):
        return Conference.objects.filter(created_by_user_id=owner_user_id)

    def increment_conference_talks_count(self, conference: Conference):
        # Atomic Increment
        conference.talks_count = F("talks_count") + 1
        conference.save(update_fields=["talks_count"])
