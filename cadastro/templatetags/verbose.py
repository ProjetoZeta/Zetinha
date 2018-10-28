from django import template
register = template.Library()

@register.simple_tag
def verbose(instance, field_name):
    """
    Returns verbose_name for a field.
    """
    return instance._meta.get_field(field_name).verbose_name

@register.simple_tag
def class_verbose(object):
    return object._meta.verbose_name.title()

@register.simple_tag
def class_verbose_plural(object):
    return object._meta.verbose_name_plural.title()
