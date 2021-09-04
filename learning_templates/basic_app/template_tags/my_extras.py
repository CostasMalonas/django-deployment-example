from django import template

register = template.Library()

# Below we see a decorator
@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all values "arg" from the string
    """
    return value.replace(arg, '')

"""
Now I should register the filter like below,
register.filter('string that I call the function', the name of the
function I made in our case cut)
"""
# register.filter('cut', cut)
