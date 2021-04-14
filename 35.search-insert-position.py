#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        time: O(len(nums))
        space: O(1)
        """
        for index in range(len(nums)):
            #print(index)
            if target <= nums[index]:
                return index
        return len(nums)

# @lc code=end

