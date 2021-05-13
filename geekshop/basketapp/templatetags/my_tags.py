from django import template

register = template.Library()


def mult(value, arg):
    """Multiplies the arg and the value"""
    return value * arg


def sub(value, arg):
    """Subtracts the arg from the value"""
    return value - arg


def div(value, arg):
    """Divides the value by the arg"""
    return value / arg


register.filter('mult', mult)
register.filter('sub', sub)
register.filter('div', div)
