#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        """
        time: O(logn)
        space: O(1)
        """
        if not n:
            return False

        while n != 1:
            if n % 2 == 1:
                return False

            n = n // 2
        return True

# @lc code=end

