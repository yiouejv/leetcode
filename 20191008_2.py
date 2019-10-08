# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
#
# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。




class Solution:
    def lengthOfLongestSubstring(self, s: str): # -> int:
        i = 0
        j = 1
        max = 0

        while j <= len(s):
            subs = s[i:j]  # 字串
            # 如果存在重复的，i后移一位
            if len(set(subs)) != len(subs):
                i += 1
            # 不存在重复的则j后移一位
            else:
                j += 1
                if len(subs) > max:
                    max = len(subs)
        return max



print(Solution().lengthOfLongestSubstring('cdd'))