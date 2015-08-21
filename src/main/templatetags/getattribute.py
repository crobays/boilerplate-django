from django import template
from django.conf import settings
from django.db.models.query import QuerySet

register = template.Library()


def getattribute(value, arg):
    """ Gets an attribute of an object dynamically from a string name """
    if isinstance(value, QuerySet) or isinstance(value, list):
        return [getattribute(x, arg) for x in value]
    elif hasattr(value, str(arg)):
        return getattr(value, arg)
    elif str(arg) in value:
        return value[arg]
    elif str(arg).isdigit() and len(value) > int(arg):
        return value[int(arg)]
    else:
        try:
            return value[arg]
        except KeyError:
            return settings.TEMPLATE_STRING_IF_INVALID

register.filter('getattribute', getattribute)

# Then, in template:
# {% load getattribute %}
# {{ object|getattribute:dynamic_string_var }}