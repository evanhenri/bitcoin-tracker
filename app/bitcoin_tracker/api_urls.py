from django.conf.urls import include, url

from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from .views import api


router = routers.DefaultRouter()
router.register('addresses', api.AddressesViewSet)

v1_patterns = [
    url(
        r'^docs/',
        include_docs_urls(
            title='Bitcoin-Tracker API',
        )
    ),
    url(r'', include(router.urls)),
]

urlpatterns = [
    url(r'^v1/', include(v1_patterns)),
]
