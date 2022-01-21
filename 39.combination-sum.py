#
# @lc app=leetcode id=39 lang=python3
#
# [39] Combination Sum
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ret = []
        self.target = target
        self.candidates = candidates
        candidates.sort()
        self.dfs(0, [], 0)
        return self.ret
    
    def dfs(self, idx, ans, sum):
        if sum == self.target:
            self.ret.append(ans.copy())
            return
        
        elif sum < self.target:
            for i in range(idx, len(self.candidates)):
                ans.append(self.candidates[i])
                self.dfs(i, ans, sum + self.candidates[i])
                ans.pop()
        
        elif sum > self.target:
            return
# @lc code=end

