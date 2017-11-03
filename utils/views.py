
'''
get_data_for_generic_table([Model Object])

This function gets the data from the model in order to fill the 'generic-table.html' template
for automatically generating that table from the passed model
'''

def get_data_for_generic_table(model, fields=[]):
    fields = fields if len(fields) else []
    if len(fields) == 0:
        for field in model._meta.get_fields():
            if field.name != 'id':
                fields.append(field.name)
    query_set = model.objects.all()
    data = []
    for item in query_set:
        items = []
        for field in fields:
            items.append(getattr(item, field))
        data.append(items)
    labels = [model._meta.get_field(field).verbose_name for field in fields]
    return {
        'fields': fields,
        'object_list': data,
        'labels': labels,
        'model_name_plural': model._meta.verbose_name_plural.capitalize(),
        'model_name': model._meta.verbose_name.capitalize()
    }
