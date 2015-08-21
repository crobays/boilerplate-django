from django import template
from django.template.base import Node
from django.templatetags.static import StaticNode
from django.templatetags.static import PrefixNode
from django.utils.encoding import iri_to_uri
from django.utils.six.moves.urllib.parse import urljoin

register = template.Library()

class StaticDistNode(StaticNode):
    @classmethod
    def handle_simple(cls, path):
        return urljoin(PrefixNode.handle_simple("APP_STATIC_DIST_URL"), path)

@register.tag('static_dist')
def do_static_dist(parser, token):
    """
    Joins the given path with the APP_STATIC_DIST_URL setting.

    Usage::

        {% static_dist path [as varname] %}

    Examples::

        {% static_dist "css/base.css" %}
        {% static_dist variable_with_path %}
        {% static_dist "css/base.css" as admin_base_css %}
        {% static_dist variable_with_path as varname %}

    """
    return StaticDistNode.handle_token(parser, token)


def static_dist(path):
    return StaticDistNode.handle_simple(path)
