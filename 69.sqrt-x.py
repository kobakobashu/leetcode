#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if not x:
            return 0

        # ans1
        """
        time: O(1)
        space: O(1)
        return int(x ** 0.5)
        """
        
        # ans2 using binary search
        """
        time: O(logx)
        space: O(1)
        """
        low = 0
        high = x + 1
        while high - low > 1:
            mid = (low + high) // 2
            if mid ** 2 <= x:
                low = mid
            else:
                high = mid
        return low
# @lc code=end
