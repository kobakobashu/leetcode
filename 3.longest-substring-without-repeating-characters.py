#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
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
        """
        """
        if len(s) <= 1:
            return len(s)

        ref = {}
        cur_max_length = 0
        start = 0
        for idx, alph in enumerate(s):
            if alph in ref:
                start = ref[alph] + 1
                cur_max_length = idx - start + 1
                ref[alph] = idx
            else:
                ref[alph] = idx
        return cur_max_length
        """
        ref = {}
        cur_max_length = 0
        start = 0
        _max = 0
        for idx, alph in enumerate(s):
            if alph in ref:
                start = ref[alph] + 1
                _max = max(_max, idx - ref[alph])
                ref[alph] = idx
            else:
                ref[alph] = idx
            cur_max_length = max(idx - start + 1, cur_max_length)
            print("max")
            print(_max)
            print("cur_max_length")
            print(cur_max_length)
        return max(_max, cur_max_length)
# @lc code=end

