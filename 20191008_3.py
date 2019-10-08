# 给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。
#
# 示例 1：
#
# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
# 示例 2：
#
# 输入: "cbbd"
# 输出: "bb"

class Solution:
    def longestPalindrome(self, s: str): # -> str:
        max = 0
        max_s = ''  # 最大的字串

        for i in range(0, len(s)):
            for j in range(i, len(s)):
                j += 1
                subs = s[i:j]

                if not len(subs) > max:
                    continue

                # 如果是回文，则保存字串长度
                if subs == subs[::-1]:
                    max = len(subs)
                    max_s = subs

            i += 1
        return max_s


print(Solution().longestPalindrome('cbbd'))







