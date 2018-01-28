"""
Basic XDict
"""

import dpath
import copy


# should match behavior of builtin dict()
dpath.options.ALLOW_EMPTY_STRING_KEYS = True


class XDict(dict):
    """Combines the basic usability of a dict with the lookup syntax of dpath"""

    def get(self, path, default=None, separator='/', allow_default=True):
        try:
            return dpath.util.get(self.copy(), path, separator)
        except KeyError:
            if allow_default:
                return default
            else:
                raise KeyError('Key not found: [{}]'.format(path))

    def search(self, path, yielded=False):
        return dpath.util.search(self.copy(), path, yielded=yielded)
