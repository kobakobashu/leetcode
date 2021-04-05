#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        """
        time: O(log x)
        space: O(1)
        """
        if x >= 0:
            x = str(x)
            output = int(x[::-1])
        else:
            x = str(-1*x)
            x = int(x[::-1])
            output = -1 * x
        if output > 2 ** 31 or output < -1 * 2 ** 31:
            return 0
        return output
        
# @lc code=end