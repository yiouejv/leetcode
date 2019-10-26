'''
    date: 2019/10/26
    path: ../数组/35....md
    email: yiouejv@126.com 
'''


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i
