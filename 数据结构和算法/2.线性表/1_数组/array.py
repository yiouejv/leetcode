'''
    date: 2019/10/30
    email: yiouejv@126.com
'''


class Array(object):

    def __init__(self, size):
        self.size = size
        self._items = [None] * size

    def __setitem__(self, key, value):
        self._items[key] = value

    def __getitem__(self, key):
        return self._items[key]

    def len(self):
        return self.size