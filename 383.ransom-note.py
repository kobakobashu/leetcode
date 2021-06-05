#
# @lc app=leetcode id=383 lang=python3
#
# [383] Ransom Note
#
import collections

# @lc code=start
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_dict = collections.Counter(ransomNote)
        magazine_dict = collections.Counter(magazine)

        for i in ransomNote_dict:
            if magazine_dict[i] < ransomNote_dict[i]:
                return False

        return True        
# @lc code=end

