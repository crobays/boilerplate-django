from django import template
from django.template.base import Node
from django.templatetags.static import StaticNode
from django.templatetags.static import PrefixNode
from django.utils.encoding import iri_to_uri
from django.utils.six.moves.urllib.parse import urljoin

register = template.Library()

class StaticImageNode(StaticNode):
    @classmethod
    def handle_simple(cls, path):
        return urljoin(PrefixNode.handle_simple("APP_STATIC_IMAGES_URL"), path)

class MediaNode(StaticNode):
    @classmethod
    def handle_simple(cls, path):
        return urljoin(PrefixNode.handle_simple("MEDIA_URL"), path)

@register.simple_tag
def image(path):
    return StaticImageNode.handle_simple(path)

@register.simple_tag
def media(path):
    return MediaNode.handle_simple(path)
