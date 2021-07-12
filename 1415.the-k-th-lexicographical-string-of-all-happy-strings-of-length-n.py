#
# @lc app=leetcode id=1415 lang=python3
#
# [1415] The k-th Lexicographical String of All Happy Strings of Length n
#
from collections import deque

# @lc code=start
class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = ['a', 'b', 'c']
        stack = deque(happy)
        m = 0

        while stack:
            m += 1
            print(m)
            curr_word = stack.popleft()
            if len(curr_word) == n:
                stack.appendleft(curr_word)
                break

            for word in happy:
                #print(stack)
                #print((curr_word))
                if curr_word[-1] != word:
                    stack.append(curr_word + word)

        if len(stack) >= k:
            return stack[k-1]
        else:
            return ''

# @lc code=end

