from django.urls import path

from talk.views import ConferenceTalkListView

# v1/conferences/<str:conference_id>/talks/
urlpatterns = [
    # v1/conferences/<str:conference_id>/talks/
    path("", ConferenceTalkListView.as_view())
]
