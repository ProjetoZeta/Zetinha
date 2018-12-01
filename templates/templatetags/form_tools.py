from django import template
register = template.Library()
import datetime

@register.simple_tag
def get_value(form, field, value):
	try:
		return dict(form.fields[field].choices)[value]
	except AttributeError:
		if form.fields[field].__class__.__name__ != 'DateField':
			return value
		else:
			date = datetime.datetime.strptime(str(value), '%Y-%m-%d').date()
			return date.strftime('%d/%m/%y')

@register.filter
def is_required (form, field):
    return form.fields[field].required





