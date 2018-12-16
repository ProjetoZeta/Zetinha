def get_clean_fields(model):
    fields = []
    for f in model._meta.get_fields():
        if not f.is_relation and not f.auto_created:
            fields.append(f.name)
    return fields

def get_fields(model, ignore=[]):
    fields = []
    for f in model._meta.get_fields():
        if not f.auto_created:
            fields.append(f.name)

    return [x for x in fields if x not in ignore]

def choice_keys_list(choices):
    return [i[0] for i in choices]