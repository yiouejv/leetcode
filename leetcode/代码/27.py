'''
    date: 2019/10/26
    path: ../数组/27....md
    email: yiouejv@126.com 
'''


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        count = 0
        for i in range(len(nums)):
            if nums[count] != val:
                nums[count] = nums[i]
                count += 1
        return count


print(Solution().removeElement([3,2,2,3], 3))