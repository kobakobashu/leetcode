#
# @lc app=leetcode id=47 lang=python3
#
# [47] Permutations II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        self.ret = []
        self.dfs(nums, [])
        return self.ret
    
    def dfs(self, nums, ans):
        if not nums:
            self.ret.append(ans.copy())
            return
        
        for idx, num in enumerate(nums):
            if idx > 0 and nums[idx - 1] == num:
                continue
            ans.append(num)
            self.dfs(nums[: idx] + nums[idx + 1:], ans)
            ans.pop()
# @lc code=end
