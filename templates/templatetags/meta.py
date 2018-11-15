from django import template
register = template.Library()

@register.filter
def model_name(instance):
    return instance.__class__.__name__.lower()


@register.filter
def is_bool(value):
    return type(value) is bool

@register.simple_tag
def get_value(form, field, value):
	try:
		return dict(form.fields[field].choices)[value]
	except AttributeError: 
		return value

