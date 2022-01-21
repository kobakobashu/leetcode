#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.dfs(nums, [])
        return self.res
    
    def dfs(self, nums, path):
        if len(nums) == 0:
            self.res.append(path.copy())
            return
        
        for i in range(len(nums)):
            path.append(nums[i])
            self.dfs(nums[:i] + nums[i + 1:], path)
            path.pop()
# @lc code=end
