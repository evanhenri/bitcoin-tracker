from celery import shared_task

from ..models import Address
from ..util import bitcoin


@shared_task
def refresh_cache():
    addresses = Address.objects.all().values_list('data', flat=True)
    bitcoin.get_balances(*addresses)
    for address in addresses:
        bitcoin.get_transactions(address)
