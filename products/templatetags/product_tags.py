from django import template
from django.conf import settings

# create your templatetags here

register = template.Library()

DOLLOR_TO_RIAL = 580000


@register.simple_tag
def converter_unit_money(value, **kwargs):
    # print(kwargs)
    if kwargs['unit'] == 'rial':
        return f'{int(value * DOLLOR_TO_RIAL)} Rial'
    else:
        return f'{value} $'
    

@register.simple_tag
def get_unit_money():
    return settings.CHOOSE_UNIT_MONEY


@register.simple_tag
def get_available_unit_money():
    for unit in settings.LIST_OF_UNIT_MONEY:
        yield unit
