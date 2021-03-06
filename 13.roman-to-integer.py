#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        """
        time: O(len(s))
        space: O(1)
        """
        ans = 0
        roman_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000,}
        for i in range(len(s)-1):
            if roman_dict[s[i]] < roman_dict[s[i+1]]:
                ans -= roman_dict[s[i]]
            else:
                ans += roman_dict[s[i]]
        ans += roman_dict[s[len(s)-1]]
        return ans
# @lc code=end

