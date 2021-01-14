from django.contrib import admin
from django.urls import (
    include,
    path,
)

from .views import (
    AddressesView,
    TransactionsView,
)


urlpatterns = [
    path('', AddressesView.as_view(), name='addresses'),
    path('address/<str:address>/', TransactionsView.as_view(), name='transactions'),
    path('admin/', admin.site.urls),
    path('api/', include('bitcoin_tracker.api_urls')),
]
