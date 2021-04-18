#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        time: O(1)
        space: O(1)
        """
        output_10 = int(a,2) + int(b,2)
        return bin(output_10).replace('0b', '')
# @lc code=end

