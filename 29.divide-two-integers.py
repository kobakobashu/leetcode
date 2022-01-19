#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        res, is_positive = 0, 0
        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0) :
            is_positive = 1
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        while dividend >= divisor:
            n = 0
            while dividend >= (divisor << n):
                n += 1
            res += 1 << (n - 1)
            dividend -= (divisor << (n - 1))
        
        if not is_positive:
            res = -res
        if res > 2147483647:
            return 2147483647
        if res < -2147483648:
            return -2147483648
        
        return res
# @lc code=end

