from django.urls import path

from talk.views import (
    ConferenceTalkListView,
    CreateTalkView,
    AddSpeakerParticipantsView,
)

# v1/conferences/<str:conference_id>/talks/
urlpatterns = [
    # v1/conferences/<str:conference_id>/talks/
    path("", ConferenceTalkListView.as_view()),
    # v1/conferences/<str:conference_id>/talks/create/
    path("create/", CreateTalkView.as_view()),
    # v1/conferences/<str:conference_id>/talks/<str:talk_id>/update/
    path(
        "<str:talk_id>/add-speaker-participant/",
        AddSpeakerParticipantsView.as_view(),
    ),
]
