#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
 
        cur = 0
        step = 0
        next_max = 0
        for idx, num in enumerate(nums):
            next_max = max(next_max, idx + num)

            if cur == idx:
                step += 1
                cur = next_max
                if cur >= len(nums) - 1:
                    return step
# @lc code=end
