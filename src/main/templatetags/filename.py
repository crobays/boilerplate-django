from django.conf import settings
import os

from django import template


register = template.Library()

@register.filter
def filename(value):
    try:
        return os.path.basename(value.file.name)
    except:
        return settings.TEMPLATE_STRING_IF_INVALID