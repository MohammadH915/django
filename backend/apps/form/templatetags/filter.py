# custom_filters.py
from django import template

register = template.Library()


@register.filter(name='is_date_field')
def is_date_field(field):
    return field.name in ['date', 'deadline']


@register.filter(name='is_description_field')
def is_description_field(field):
    return field.name == 'description'
