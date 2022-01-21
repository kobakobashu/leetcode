#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        int_num1 = 0
        for i in range(len(num1)):
            int_num1 += 10 ** (len(num1) - i - 1) * (ord(num1[i]) - ord("0"))
        
        int_num2 = 0
        for i in range(len(num2)):
            int_num2 += 10 ** (len(num2) - i - 1) * (ord(num2[i]) - ord("0"))
        
        return str(int_num1 * int_num2)
# @lc code=end
