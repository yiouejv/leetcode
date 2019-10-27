'''
    date: 2019/10/26
    path: ../线性表/3.链表下....md
    email: yiouejv@126.com 
'''


class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return '<value {value} next{next}>'.format(value=self.value, next=self.next)


class LinkList(object):
    '''单链表'''
    def __init__(self):
        node = Node()
        self.root = node
        self.headnode = None
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        node = Node(value=value)

        if len(self) == 0:
            self.headnode = node
            self.root.next = self.headnode
        else:
            self.tailnode.next = node

        self.tailnode = node
        self.length += 1

    def __iter__(self):
        curnode = self.headnode

        while curnode and curnode != self.tailnode:
            yield curnode.value
            curnode = curnode.next

        if curnode is not None:
            yield curnode.value

    def pop(self):
        if not len(self):
            raise Exception('from empty linklist pop')

        prenode = self.root
        curnode = prenode.next

        while curnode != self.tailnode:
            prenode = prenode.next
            curnode = curnode.next

        value = self.tailnode.value
        del curnode
        prenode.next = None
        self.tailnode = prenode
        return value

    def appendleft(self, value):
        if len(self) == 0:
            self.append(value)
        else:
            node = Node(value)
            node.next = self.root.next
            self.root.next = node
            self.headnode = node
            self.length += 1

    def remove(self, value):
        if not self:
            raise Exception('from empty linklist remove')

        if value not in self:  # 不在链表里什么都不做
            return

        prenode = self.root
        curnode = prenode.next
        while curnode.value != value:
            prenode = prenode.next
            curnode = curnode.next

        prenode.next = curnode.next
        if curnode == self.tailnode:
            self.tailnode = prenode

        if curnode == self.headnode:
            self.headnode = curnode.next

        del curnode
        self.length -= 1


def test_linklist():
    # ll = LinkList()
    # ll.append(1)
    # ll.append(2)
    # ll.append(3)
    # ll.append(4)
    # ll.append(5)
    #
    # assert list(ll) == [1, 2, 3, 4, 5]
    #
    # assert ll.pop() == 5
    # assert ll.pop() == 4
    # assert ll.pop() == 3
    #
    # ll.appendleft(0)
    # assert list(ll) == [0, 1, 2]
    #
    # ll.appendleft(-1)
    # assert list(ll) == [-1, 0, 1, 2]
    #
    # ll.remove(0)
    # assert list(ll) == [-1, 1, 2]
    #
    # ll.remove(0)
    # assert list(ll) == [-1, 1, 2]
    #
    # ll.remove(2)
    # assert list(ll) == [-1, 1]
    #
    # ll.remove(-1)
    # assert list(ll) == [1]
    #
    # ll.remove(1)
    # assert list(ll) == []
    #
    ll = LinkList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    ll.append(5)

    assert list(ll) == [1, 2, 3, 4, 5]
    ll.reverse()
    assert list(ll) == [5, 4, 3, 2, 1]

test_linklist()