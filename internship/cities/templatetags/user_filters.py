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
