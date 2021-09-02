from django.urls import path

from conference.views import ConferenceListView, CreateConferenceView

# v1/conferences/
urlpatterns = [
    # v1/conferences/
    path("", ConferenceListView.as_view()),
    # v1/conferences/create/
    path("create/", CreateConferenceView.as_view()),
]
