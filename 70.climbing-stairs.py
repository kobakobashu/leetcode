#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        time: O(n)
        space: O(n)
        """
        step = [0]*(n+2)
        step[0] = 0
        step[1] = 1
        step[2] = 2
        if 3 <= n:
            for step_num in range(3,n+1):
                step[step_num] = step[step_num - 1] + step[step_num - 2]
        return step[n]
# @lc code=end

