from django.core.exceptions import ValidationError
from conference.serializers.conference_serializer import ConferenceSerializer
from conference.services import ConferenceService
from common.base_view import BaseView
from rest_framework.pagination import LimitOffsetPagination


class ConferenceListView(BaseView):
    conference_service = ConferenceService()
    paginator = LimitOffsetPagination()
    serializer = ConferenceSerializer

    def get(self, request):
        conference_admin_id = request.query_params.get("conference_admin", None)
        try:
            if conference_admin_id:
                conference_queryset = (
                    self.conference_service.get_conferences_by_owner_id(
                        conference_admin_id
                    )
                )
            else:
                conference_queryset = self.conference_service.get_conferences()
        except ValidationError as error:
            return self.bad_request_response(error.message)

        paginated_conference_queryset = self.paginator.paginate_queryset(
            conference_queryset, request
        )
        conference_data = self.serializer(paginated_conference_queryset, many=True).data
        return self.paginated_response(self.paginator, "Conferences", conference_data)
