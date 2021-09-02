from django.urls import path

from conference.views import (
    ConferenceListView,
    CreateConferenceView,
    UpdateConferenceView,
)

# v1/conferences/
urlpatterns = [
    # v1/conferences/
    path("", ConferenceListView.as_view()),
    # v1/conferences/create/
    path("create/", CreateConferenceView.as_view()),
    # v1/conferences/update/
    path("<str:conference_id>/update/", UpdateConferenceView.as_view()),
]
