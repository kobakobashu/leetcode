#
# @lc app=leetcode id=434 lang=python3
#
# [434] Number of Segments in a String
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        """
        time complexity : O(len(s))
        space complexity : O(1)
        """
        if not s:
            return 0

        return sum(s[i] != ' ' and (i == 0 or s[i - 1] == ' ') for i in range(len(s)))
        

        """
        time complexity : O(len(s))
        space complexity : O(1)
        
        if not s:
            return 0

        return len([i for i in s.split(" ")])
        """
# @lc code=end
