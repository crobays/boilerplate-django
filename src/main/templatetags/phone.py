from django import template
import re

register = template.Library()

@register.filter
def phone(string):
    return re.sub(r'[^\+\w\d]', '', string)