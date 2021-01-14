from django.conf import settings
from rest_framework.viewsets import ModelViewSet

from ...models import Address
from ...serializers import AddressSerializer


class AddressesViewSet(ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

    def destroy(self, request, *args, **kwargs):
        address = Address.objects.get(pk=kwargs['pk'])
        settings.REDIS.delete(
            f'{address}_balance',
            f'{address}_transactions',
        )
        return super().destroy(request, *args, **kwargs)
