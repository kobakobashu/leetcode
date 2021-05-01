#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        time: O(len(prices))
        space: O(len(prices))
        """
        if not prices:
            return ""

        min_price = prices[0]
        profit = 0
        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)
        return profit
# @lc code=end

