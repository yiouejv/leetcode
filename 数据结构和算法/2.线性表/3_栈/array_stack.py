'''
    date: 2019/10/29
    email: yiouejv@126.com
    顺序栈：数组实现的栈
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


class ArrayStack(Array):
    def __init__(self, size):
        self.size = size
        self._items = Array(size)
        self.top = -1

    def __len__(self):
        return self.size

    def is_empty(self):
        return True if self.top < 0 else False

    def push(self, value):
        if self.top >= len(self):
            raise Exception('stack is full')

        self.top += 1
        self._items[self.top] = value

    def pop(self):
        if self.is_empty():
            raise Exception('stack is empty')

        v = self._items[self.top]
        self._items[self.top] = None
        self.top -= 1
        return v


def test_array_stack():
    stack = ArrayStack(5)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert len(stack) == 5
    assert stack.is_empty() == False
    assert stack.pop() == 5
    assert stack.pop() == 4
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert stack.is_empty() == True






