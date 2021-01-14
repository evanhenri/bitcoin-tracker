from django import template


register = template.Library()


@register.filter
def get_item(dictionary, key):
    return dictionary[key]


@register.filter
def satoshis_to_btc(satoshis):
    return f'{int(satoshis) / 10 ** 8:,.8f}'
