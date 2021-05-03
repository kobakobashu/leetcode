#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time: O(len(prices))
        space: O(1)
        """
        sum_profit_to_day = 0
        pre_price = prices[0]
        for day in range(1, len(prices)):
            if pre_price <= prices[day]:
                sum_profit_to_day += (prices[day] - pre_price)
            pre_price = prices[day]
        return sum_profit_to_day
                
# @lc code=end

