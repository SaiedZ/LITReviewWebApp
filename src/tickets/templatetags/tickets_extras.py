from django.template import Library

register = Library()


@register.filter
def get_range(value, arg=None):
    """create a range"""
    return range(value) if not arg else range(value, arg)
