from django.core.urlresolvers import reverse
import re
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def active(context, pattern, class_name='active'):
    """
    Return active when request path matches pattern
    """
    request = context.get('request')
    if request and re.search(pattern, request.path):
        return class_name
    return ''


@register.simple_tag(takes_context=True)
def active_reverse(context, name, class_name='active'):
    """
    Return active when request path matches pattern
    """
    request = context.get('request')
    if not request:
        return ''

    path = reverse(name, getattr(request, 'subdomain', None))
    if path == "/":
        if request.path == "/":
            return class_name
        return ''
    
    if re.search(
        '^%s' % re.sub(r'^https?://[^/]+',
        '',
        path),
        request.path
    ):
        return class_name

    return ''