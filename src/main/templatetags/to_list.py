from django import template


register = template.Library()

@register.filter
def to_list(val):
    if not isinstance(val, list):
        return [val]
    return val