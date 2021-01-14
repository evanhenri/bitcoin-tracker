from django.urls import reverse
from django.views.generic import CreateView

from ..forms import AddressForm
from ..models import Address
from ..util import bitcoin

__all__ = ['AddressesView']


class AddressesView(CreateView):
    template_name = 'bitcoin_tracker/addresses.html'
    form_class = AddressForm
    model = Address

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Address.objects.all()
        context['balances'] = bitcoin.get_balances(
            *Address.objects.all().values_list('data', flat=True),
            use_cache=True
        )
        return context

    def get_success_url(self):
        return reverse('addresses')
