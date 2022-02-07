from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def add_image(value):
    if value:
        result = '<img src="/media/icons/icon-yes.svg">'
    else:
        result = '<img src="/media/icons/icon-no.svg">'
    return mark_safe(result)


@register.filter
def addclass(field, css):
    return field.as_widget(attrs={"class": css})


@register.simple_tag
def relative_url(value, field_name, urlencode=None):
    url = f'?{field_name}={value}'
    if urlencode:
        querystring = urlencode.split('&')
        filtered_querystring = filter(lambda p: p.split('=')[0] != field_name, querystring)
        encoded_querystring = '&'.join(filtered_querystring)
        url = f'{url}&{encoded_querystring}'
    return url
