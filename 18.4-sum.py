#
# @lc app=leetcode id=18 lang=python3
#
# [18] 4Sum
#

# @lc code=start
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) <= 3:
            return None

        nums.sort()
        output_4_nums = []
        i = 0
        while i < len(nums) - 3:
            j = i + 1
            while j < len(nums) - 2:
                left = j + 1
                right = len(nums) - 1
                while left < right:
                    cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    print(cur_sum)
                    if cur_sum < target:
                        left += 1
                    elif cur_sum > target:
                        right -= 1
                    else:
                        cur_4_nums = [nums[i], nums[j], nums[left], nums[right]]
                        while left < right - 1 and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right - 1 and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                        output_4_nums.append(cur_4_nums)
                while j < len(nums) - 3 and nums[j] == nums[j+1]:
                    j += 1
                j += 1
            while i < len(nums) - 4 and nums[i] == nums[i + 1]:
                i += 1
            i += 1
        return output_4_nums
# @lc code=end

