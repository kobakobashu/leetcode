#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        time: O(rowIndex^2)
        space: O(rowIndex^2)
        """
        cur_Row_list = [1]
        for Row in range(2, rowIndex + 2):
            cur_Row_list = [1]
            for cul_num in range(1, Row - 1):
                cur_Row_list.append(pre_Row_list[cul_num - 1] + pre_Row_list[cul_num])
            cur_Row_list.append(1)
            pre_Row_list = cur_Row_list
        return cur_Row_list
# @lc code=end

