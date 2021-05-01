#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        """
        time: O((n+m)log(n+m))
        space: O(1)  if (len(nums1) - m) > n
             : O(n)  else
        """
        nums1[m:] = nums2
        nums1.sort()
        
# @lc code=end