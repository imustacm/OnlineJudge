def to_dict_tools(target):
    data = dict()
    attribute = dir(target)
    if 'public_info' in attribute:
        public_info = getattr(target, 'public_info')
    attribute = dir(target)
    for item in attribute:
        item = str(item)
        if not item.startswith('_') and item in public_info:
            data[item] = str(getattr(target, item))
    return data
