from django.core.exceptions import ValidationError
from rest_framework.pagination import LimitOffsetPagination

from common.base_view import BaseView
from talk.serializers import TalkSerializer
from talk.services import TalkService


class ConferenceTalkListView(BaseView):
    paginator = LimitOffsetPagination()
    talk_service = TalkService()
    serializer = TalkSerializer

    def get(self, request, conference_id):
        try:
            talks_queryset = self.talk_service.get_talks_by_conference_id(conference_id)
        except ValidationError as error:
            return self.bad_request_response(error.message)

        paginated_talk_queryset = self.paginator.paginate_queryset(
            talks_queryset, request
        )
        talks_data = self.serializer(paginated_talk_queryset, many=True).data
        return self.paginated_response(self.paginator, "Talks", talks_data)
