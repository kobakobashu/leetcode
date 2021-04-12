#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        time: O(len(nums))
        space: O(1)
        """
        if len(nums) == 0:
            return 0
        len_output = 0
        for cur_input in range(1, len(nums)):
            if nums[cur_input] != nums[len_output]:
                len_output += 1
                nums[len_output] = nums[cur_input]
        return len_output + 1

# @lc code=end

