#
# @lc app=leetcode id=40 lang=python3
#
# [40] Combination Sum II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.ret = []
        self.candidates = candidates
        self.target = target
        self.dfs(0, [], 0)
        return self.ret
    
    def dfs(self, idx, ans, sum_ans):
        if sum_ans == self.target:
            if not self.ret or self.ret[-1] != ans:
                self.ret.append(ans.copy())
            return
        
        elif sum_ans < self.target:
            for i in range(idx, len(self.candidates)):
                if i > idx and self.candidates[i] == self.candidates[i - 1]:
                    continue
                ans.append(self.candidates[i])
                self.dfs(i + 1, ans, sum_ans + self.candidates[i])
                ans.pop()
        
        else: 
            return 
# @lc code=end

