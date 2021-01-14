from django.views.generic import TemplateView

from ..util import bitcoin

__all__ = ['TransactionsView']


class TransactionsView(TemplateView):
    template_name = 'bitcoin_tracker/transactions.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address = kwargs['address']
        context['transactions'] = bitcoin.get_transactions(address, use_cache=True)
        return context
