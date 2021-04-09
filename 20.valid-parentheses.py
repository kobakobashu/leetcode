#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        """
        time: O(len(s))
        space: O(len(s))
        """
        stack = []
        brackets_dict = {")" : "(" , "}" : "{" , "]" : "[", }
        for char in s:
            if char in brackets_dict.values():
                stack.append(char)
            elif char in brackets_dict.keys():
                if len(stack) == 0 or brackets_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

# @lc code=end

