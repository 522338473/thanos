from django.template import Library
from django.utils.safestring import mark_safe

register = Library()


@register.inclusion_tag
def show(n):
    pass
