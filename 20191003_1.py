# 给定一个正整数，返回它在 Excel 表中相对应的列名称。
#
# 例如，
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB
#     ...
# 示例 1:
#
# 输入: 1
# 输出: "A"
# 示例 2:
#
# 输入: 28
# 输出: "AB"
# 示例 3:
#
# 输入: 701
# 输出: "ZY"

import string


class Solution:
    def __init__(self):
        self.dic = dict(zip(range(1, 27), string.ascii_uppercase))
        self.dic[0] = ''

    def convertToTitle(self, n: int):
        if n <= 26:
            return self.dic[n]
        return ''.join(['A', self.convertToTitle(n - 26)])


print(Solution().convertToTitle(100))