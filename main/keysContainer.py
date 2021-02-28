class KeysContainer:
    def __init__(self, iter):
        self._keys = {key: False for key in iter}

    def __getattr__(self, item):
        if hasattr(self._keys, item):
            return getattr(self._keys, item)
        elif item in self._keys.keys():
            return self._keys[item]

    def __getitem__(self, item):
        return self._keys[item]

    def __setitem__(self, key, value):
        self._keys[key] = value

    def __iter__(self):
        return iter(self._keys.keys())

    def __repr__(self):
        return repr(self._keys)
