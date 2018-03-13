def get_key_to_hash(prefix, *args, **kwargs):
    """Return key to hash for *args and **kwargs."""
    key_to_hash = prefix
    # First args
    for i in args:
        key_to_hash += ":%s" % i
    # Attach any kwargs
    for key in sorted(kwargs.keys()):
        key_to_hash += ":%s" % kwargs[key]
    return key_to_hash
