'''
    date: 2019/10/28
    path: ../数组/11....md
    email: yiouejv@126.com 
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # 题目的意思：两个数组元素的下标相减再乘以这两个数组元素的较小值。找出最大的值。
        # 方法一：暴力遍历
        #      求出所有的情况，取最大,
        #      时间复杂度 O(n**2)
        #      空间复杂度 O(1)
        #       超出时间限制，此方法不耐用
        # max = 0
        # for i in range(len(height)-1):
        #     for j in range(i+1, len(height)):
        #         r =  (j-i) * min(height[i], height[j])
        #         if r > max:
        #             max = r
        # return max
        # 方法二：
        #    双指针法，首尾两个指针保证了宽度由大到小，首位两个指针向中间靠拢。
        #    靠拢规则：指向较小数的指针王中间靠拢，直到尾指针小于等于首指针。保存之间最大的面积
        #    时间复杂度： O(n)
        #    空间复杂度： O(1)
        max = 0
        i = 0
        j = len(height) - 1
        while j > i:
            r = (j - i) * min(height[i], height[j])
            if r > max:
                max = r

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max


print(Solution().maxArea([2,3,4,5,18,17,6]))