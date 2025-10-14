from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("polls/", include("polls.urls")),
    # Add a redirect from root to polls
    path("", RedirectView.as_view(url="/polls/", permanent=True)),
]
