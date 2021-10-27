#
# @lc app=leetcode id=1672 lang=python3
#
# [1672] Richest Customer Wealth
#

# @lc code=start
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        if not accounts:
            return None
        
        max_money = sum(accounts[0])
        for money_list in accounts:
            money_list_sum = sum(money_list)
            max_money = max(money_list_sum, max)
        
        return max_money
# @lc code=end

