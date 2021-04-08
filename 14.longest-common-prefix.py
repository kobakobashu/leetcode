#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        time: O(S) S: sum of the all characters
        space: O(1)
        """
        n = len(strs)
        if n == 0:
            return ""
        min_len = len(min(strs, key=len))
        flag = 1
        ans = ""
        for i in range(min_len):
            for j in range(len(strs)):
                if strs[j][i] != strs[0][i]:
                    flag = 0
            if flag == 1:
                ans += strs[0][i]
        return (ans)
# @lc code=end

