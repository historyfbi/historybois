from django import template

register = template.Library()


@register.filter()
def add_xx(value):
    return '%sxx' % value
