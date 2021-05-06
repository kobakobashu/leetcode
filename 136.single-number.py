#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        time: O(nlogn) n: len(nums)
        space: O(n)
        """
        if not nums:
            return None

        nums.sort()
        for num in range(0, len(nums) - 1, 2):
            if nums[num] != nums[num + 1]:
                return nums[num]

        return nums[-1]
# @lc code=end

