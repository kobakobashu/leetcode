#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        ref = {}
        cur_max_length = 0
        first_repeat_position = 0
        last_repeat_position = 0
        for i in range(len(s)):
            #print(s[i])
            if not s[i] in ref:
                ref[s[i]] = i
                #print(ref)
            else:
                if first_repeat_position == 0:
                    first_repeat_position = i
                cur_max_length = max(cur_max_length, int(i - ref[s[i]]))
                ref[s[i]] = i
                last_repeat_position = i
                #print(ref)
            print(ref)
        #if cur_max_length == 0:
        #    return len(s)
        
        return max(cur_max_length, len(s) - last_repeat_position, first_repeat_position)
        
# @lc code=end

