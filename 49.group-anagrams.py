#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
from collections import defaultdict


# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        anagram_dict = defaultdict(list)
        for word in strs:
            anagram_dict["".join(sorted(word))].append(word)

        for value in anagram_dict.values():
            ans.append(value)
        
        return ans
# @lc code=end
