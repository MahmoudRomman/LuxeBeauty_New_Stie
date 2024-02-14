# custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_image_name')
def get_image_name(value):
    return value.split('/')[-1]
