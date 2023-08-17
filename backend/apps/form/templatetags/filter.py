# custom_filters.py
from django import template

register = template.Library()


@register.filter(name='is_date_field')
def is_date_field(field):
    return field.name in ['date', 'deadline']


@register.filter(name='is_note_field')
def is_note_field(field):
    return field.name == 'note'
