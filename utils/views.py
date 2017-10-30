'''
get_data_for_generic_table([Model Object])

This function gets the data from the model in order to fill the 'generic-table.html' template
for automatically generating that table from the passed model
'''

def get_data_for_generic_table(model):
    query_set = model.objects.all()
    fields = model._meta.get_fields()
    data = []
    for item in query_set:
        items = []
        for field in fields:
            items.append((getattr(item, field.name)))
        data.append(items)
    return {
        'fields': fields,
        'object_list': data,
        'model_name_plural': model._meta.verbose_name_plural.capitalize(),
        'model_name': model._meta.verbose_name.capitalize()
    }