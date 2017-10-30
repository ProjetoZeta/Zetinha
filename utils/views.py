def translate_model(model):
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
        'title': model._meta.verbose_name_plural.capitalize()
    }