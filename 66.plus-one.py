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
        number_str = ""
        for digit in digits:
            number_str += str(digit)
        output_num = int(number_str) + 1
        output = []
        for digit in str(output_num):
            output.append(digit)
        return output
        """

        """
        time: O(len(digits))
        space: O(len(digits))  
        """     
        number_str = ""
        digit_list = []
        for digit in digits:
            digit_list.append(str(digit))
        output_num = int(''.join(digit_list)) + 1
        return list(str(output_num))
        
# @lc code=end

