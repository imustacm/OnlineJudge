not_need = ['query', 'query_class', 'metadata', 'to_dict']


def to_dict_tools(target):
    data = dict()
    attribute = dir(target)
    for item in attribute:
        item = str(item)
        if not item.startswith('_') and item not in not_need:
            data[item] = str(getattr(target, item))
    return data
