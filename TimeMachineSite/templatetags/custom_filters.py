from django import template

register = template.Library()

@register.filter(name='remove_value')
def remove_value(value, arg):
    """
    This cuts out all values of "arg" from the string!
    """
    return value.replace(arg,'')