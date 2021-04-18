#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        time: 
        O(len(needle))  if len(haystack) == len(needle)
        O(1)            else
        space: O(len(needle))
        """
        if not needle:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            haystack_part = haystack[i: i + len(needle)]
            if  haystack_part == needle:
                return i
        return -1

        
# @lc code=end

