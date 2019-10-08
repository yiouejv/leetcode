# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        l1_num = self.get_num(l1)
        l2_num = self.get_num(l2)

        res = l1_num + l2_num
        res_str = str(res)[::-1]

        i = 0
        ln = ListNode(int(res_str[i:i+1]))
        cur = ln
        try:
            while True:
                i += 1
                v = int(res_str[i:i+1])
                cur.next = ListNode(v)
                cur = cur.next
        except Exception:
            return ln

    def get_num(self, l):
        num = 0
        i = 1  # 个位：1 十位: 10  百位: 100
        while True:
            num += l.val * i  # 2  2+40 42+
            i *= 10  # 10 100

            if l.next is None:
                break

            l = l.next
        return num





