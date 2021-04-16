#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        time: O(len(digits))
        space: O(len(digits))
        """
        number_str = ""
        for digit in digits:
            number_str += str(digit)
        output_num = int(number_str) + 1
        output = []
        for digit in str(output_num):
            output.append(digit)
        return output
        
# @lc code=end

