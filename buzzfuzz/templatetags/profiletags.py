from datetime import date
from django import template

register = template.Library()


@register.simple_tag
def status(profile):
    if int((date.today() - profile.birthday).days / 365) > 13:
        return 'allowed'
    else:
        return 'blocked'


@register.simple_tag
def bizzfuzz(profile):
    if profile.random % 3 is 0:
        return 'Bizz'
    elif profile.random % 5 is 0:
        return 'Fuzz'
    elif profile.random % 3 is 0 and profile.random % 5 is 0:
        return 'BizzFuzz'
    else:
        return profile.random
