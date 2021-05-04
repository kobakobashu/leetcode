#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#

# @lc code=start
class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        time: O(len(s))
        space: O(len(s))
        """
        only_alphabet_num_list = []
        for word in s.lower():
            if word.isalnum():
                only_alphabet_num_list.append(word)
        return only_alphabet_num_list == only_alphabet_num_list[::-1]
# @lc code=end

