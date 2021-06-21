#
# @lc app=leetcode id=1806 lang=python3
#
# [1806] Minimum Number of Operations to Reinitialize a Permutation
#

# @lc code=start
class Solution:
    def reinitializePermutation(self, n: int) -> int:
        distinguish_idx = 1
        ans = 0

        while ans == 0 or distinguish_idx != 1:
            distinguish_idx = 2*distinguish_idx
            if distinguish_idx >= n - 1:
                distinguish_idx -= n - 1
            ans += 1

        return ans
# @lc code=end
