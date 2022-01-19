#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
import copy

from collections import deque
from typing import List


# @lc code=start
class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        """Function to generate all combinations of well-formed parentheses
        Args:
            n(int): integer
        Returns:
            List[str]: all combinations of well-formed parentheses
        """
        ans = []
        queue = deque()
        queue.append([0, 0, []])
        while queue:
            left, right, s = queue.popleft()
            if len(s) == 2 * n:
                ans.append("".join(s))
            if left > right:
                copy_s = copy.deepcopy(s)
                if left < n:
                    s.append("(")
                    queue.append([left + 1, right, s])
                if right < n:
                    copy_s.append(")")
                    queue.append([left, right + 1, copy_s])
            elif left == right:
                copy_s = copy.deepcopy(s)
                if left < n:
                    s.append("(")
                    queue.append([left + 1, right, s])

        return ans


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        self.backtrack([], 0, 0)
        return self.ans
    
    def backtrack(self, s_list: List, left: int, right: int) -> None:
        if len(s_list) == 2 * self.n:
            self.ans.append("".join(s_list))
            return
        
        copy_s = copy.deepcopy(s_list)
        if left < self.n:
            s_list.append("(")
            self.backtrack(s_list, left + 1, right)
        if right < left:
            copy_s.append(")")
            self.backtrack(copy_s, left, right + 1)
# @lc code=end
