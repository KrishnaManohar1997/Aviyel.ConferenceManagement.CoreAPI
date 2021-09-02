from conference.serializers.conference_serializer import CreateConferenceSerializer
from conference.services import ConferenceService
from common.base_view import BaseView


class CreateConferenceView(BaseView):
    conference_service = ConferenceService()
    serializer = CreateConferenceSerializer

    def post(self, request):
        if request.user.is_authenticated:
            request.data["created_by_user"] = request.user
        conference_create_serializer = self.serializer(data=request.data)
        if not conference_create_serializer.is_valid():
            return self.serializer_error_response(
                "Conference Creation failed", conference_create_serializer.errors
            )
        conference = conference_create_serializer.save()
        return self.resource_created_response("Conference", conference.id)
