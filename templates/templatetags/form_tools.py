from django import template
register = template.Library()

@register.simple_tag
def get_value(form, field, value):
	try:
		return dict(form.fields[field].choices)[value]
	except AttributeError: 
		return value

@register.filter
def is_required (form, field):
    return form.fields[field].required





