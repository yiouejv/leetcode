'''
    date: 2019/10/28
    path: ../数组/24....md
    email: yiouejv@126.com 
'''


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '<v: {v}, n: {n}>'.format(v=self.val, n=self.next)


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        nex = cur.next

        while nex:
            cur.next = nex.next
            nex.next = cur
            pre.next = nex

            pre = nex.next
            cur = pre.next
            nex = pre.next.next
        return dummy.next


if __name__ == '__main__':
    head = ListNode(1)
    cur = ListNode(2)
    head.next = cur
    for i in range(3, 5):
        node = ListNode(i)
        cur.next = node
        cur = cur.next

    print(Solution().swapPairs(head))