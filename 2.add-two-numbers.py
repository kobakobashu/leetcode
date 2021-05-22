#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_output = ListNode()
        output = cur_output
        while l1 or l2:
            cur_output.val = l1.val + l2.val
            cur_output = cur_output.next
            l1 = l1.next
            l2 = l2.next
        return output
# @lc code=end

