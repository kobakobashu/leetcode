#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        n: len(nums)
        time: O(n)
        space: O(1)
        """
        sum_to_end = -10**5
        output = -10**5
        for end in range(len(nums)):
            sum_to_end = max(nums[end], nums[end] + sum_to_end)
            output = max(output, sum_to_end)
        return output
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        n: len(nums)
        time: O(n**2)
        space: O(1)
        
        output = nums[0]
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                #print("start", start)
                #print("end", end)
                output = max(output, sum(nums[start : end + 1]))
        print(output)
        return output
"""

# @lc code=end

