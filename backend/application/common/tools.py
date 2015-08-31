class Map(dict):
    """
    Utility class for accessing dict with dot notation
    Example:
    m = Map({"key1": 1, "key2": 2})
    """
    def __init__(self, d=None, **kwargs):
        super(Map, self).__init__(d, **kwargs)
        if d is None:
            d = {}
        if kwargs:
            d.update(**kwargs)
        for k, v in d.items():
            setattr(self, k, v)
        # Class attributes
        for k in self.__class__.__dict__.keys():
            if not (k.startswith('__') and k.endswith('__')):
                setattr(self, k, getattr(self, k))

    def __setattr__(self, name, value):
        if isinstance(value, (list, tuple)):
            value = [self.__class__(x)
                     if isinstance(x, dict) else x for x in value]
        else:
            value = self.__class__(value) if isinstance(value, dict) else value
        super(Map, self).__setattr__(name, value)
        super(Map, self).__setitem__(name, value)

    __setitem__ = __setattr__
