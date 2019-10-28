'''
    date: 2019/10/28
    path: ../数组/206....md
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
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy
        cur = pre.next
        nex = cur.next

        while cur:
            cur.next = pre
            pre = cur
            cur = nex
            nex = nex.next

        return pre


if __name__ == '__main__':
    head = ListNode(1)
    cur = ListNode(2)
    head.next = cur
    for i in range(3, 6):
        node = ListNode(i)
        cur.next = node
        cur = cur.next

    print(Solution().reverseList(head))