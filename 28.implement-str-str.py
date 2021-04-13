#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        time: O(len(haystack))
        space: O(len(haystack))
        """
        if not needle:
            return 0
        len_needle = len(needle)
        len_haystack = len(haystack)

        for i in range(len_haystack - len_needle + 1):
            haystack_part = haystack[i:i+len_needle]
            if  haystack_part == needle:
                return i
        return -1

        
# @lc code=end

