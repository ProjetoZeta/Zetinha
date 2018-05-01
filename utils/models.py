def get_clean_fields(model):
    fields = []
    for f in model._meta.get_fields():
        if not f.is_relation and not f.auto_created:
            fields.append(f.name)
    return fields

def get_fields(model):
    fields = []
    for f in model._meta.get_fields():
        if not f.auto_created:
            fields.append(f.name)
    return fields