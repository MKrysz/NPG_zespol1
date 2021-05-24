import collections

class MatDict(collections.MutableMapping):
    def __init__(self, maxlen, *a, **k):
        self.maxlen = maxlen
        self.d = dict(*a, **k)
        while len(self) > maxlen:
            self.popitem()
    def __iter__(self):
        return iter(self.d)
    def __len__(self):
        return len(self.d)
    

d = MatDict(10)
