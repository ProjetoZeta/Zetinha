def get_fields(model):
    fields = []
    for f in model._meta.get_fields():
        if not f.is_relation:
            fields.append(f.name)
    return fields