import pickle

import requests

from django.conf import settings


def get_balances(*addresses, use_cache=False):
    retval = {}

    if use_cache:
        for address in addresses:
            balance = settings.REDIS.get(f'{address}_balance')
            if balance is not None:
                retval[address] = balance

    if set(addresses) != set(retval) and addresses:
        resp = requests.get(
            f'https://api.blockchair.com/bitcoin/addresses/balances?addresses={",".join(addresses)}'
        )
        resp.raise_for_status()
        data = resp.json()['data'] or {}
        for address, satoshis in data.items():
            retval[address] = satoshis
            settings.REDIS.set(f'{address}_balance', satoshis)
    return retval


def get_transactions(address, use_cache=False):
    retval = []

    if use_cache:
        transactions = settings.REDIS.get(f'{address}_transactions')
        if transactions:
            retval = pickle.loads(transactions)

    if not retval:
        resp = requests.get(
            f'https://bch-chain.api.btc.com/v3/address/{address}/tx'
        )
        try:
            resp.raise_for_status()
        except requests.HTTPError:
            retval = []
        else:
            retval = resp.json()['data']['list']
        settings.REDIS.set(
            f'{address}_transactions',
            pickle.dumps(retval)
        )
    return retval
