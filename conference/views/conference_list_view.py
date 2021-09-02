from conference.serializers.conference_serializer import ConferenceSerializer
from conference.services import ConferenceService
from common.base_view import BaseView
from rest_framework.pagination import LimitOffsetPagination


class ConferenceListView(BaseView):
    conference_service = ConferenceService()
    paginator = LimitOffsetPagination()
    serializer = ConferenceSerializer

    def post(self, request):
        conference_queryset = self.conference_service.get_conferences()
        paginated_conference_queryset = self.paginator.paginate_queryset(
            conference_queryset, request
        )
        conference_data = self.serializer(paginated_conference_queryset, many=True)
        return self.paginated_response(self.paginator, "Conferences", conference_data)
