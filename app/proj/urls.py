from django.urls import (
    include,
    path,
)

urlpatterns = [
    path('', include('bitcoin_tracker.urls')),
]
