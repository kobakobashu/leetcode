#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        time: O(len(a)+len(b))
        space: O(1)
        """
        return bin(int(a,2) + int(b,2)).replace('0b', '')
# @lc code=end

