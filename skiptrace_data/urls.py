
from .views import *
from django.urls import path, include

urlpatterns = [
    path(
        "skip_trace",
        SkipTraceView.as_view({"post": "create"}),
        name="skip_trace",
    ),
]
