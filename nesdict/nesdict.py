"""
Basic NesDict
"""

from collections import UserDict

import dpath

# should match behavior of builtin dict()
dpath.options.ALLOW_EMPTY_STRING_KEYS = True


class NesDict(UserDict):
    """Combines the basic usability of a dict with the lookup syntax of dpath"""

    def __init__(self, *args, **kwargs):
        super().__init__()
        if not kwargs \
                and len(args) == 1 \
                and type(args[0]) == type(self):
            # special exception for using NesDict(NesDict()) without any other arguments
            self.data = args[0].data.copy()
        else:
            self.data = dict(*args, **kwargs)

    def copy(self):
        return NesDict(self.data)

    def get(self, path, default=None, allow_default=True):
        try:
            return dpath.util.get(self.data, path)
        except KeyError:
            if allow_default:
                return default
            else:
                raise KeyError('Key not found: [{}]'.format(path))

    def search(self, path, yielded=False):
        return dpath.util.search(self.data, path, yielded=yielded)

    def set(self, path, val):
        dpath.util.new(self.data, path, val)

    def setdefault(self, path, val):
        if not dpath.util.search(self.data, path):
            dpath.util.new(self.data, path, val)

    def keys(self, glob='**'):
        return [x[0] for x in self.search(glob, yielded=True)]

    def values(self, glob='**'):
        return dpath.util.values(self.data, glob)

    def items(self, glob='**'):
        return [x for x in self.search(glob, yielded=True)]

    def __getitem__(self, path):
        return self.get(path, allow_default=False)

    def __setitem__(self, path, val):
        self.set(path, val)

    def __contains__(self, path):
        return bool(self.search(path))

    def __delitem__(self, path):
        try:
            self.data.__delitem__(path)
        except KeyError:
            cmp = path.split('/')
            if len(cmp) > 1:
                parent = self.get(cmp[:-1])
                if parent:
                    del parent[cmp[-1]]
                    self.set(cmp[:-1], parent)
                else:
                    raise
            else:
                raise
