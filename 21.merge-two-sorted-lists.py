#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        output = ListNode(0)
        output_add = output
        while l1 and l2:
            if l1.val <= l2.val:
                output_add.next = ListNode(l1.val)
                l1 = l1.next
            else:
                output_add.next = ListNode(l2.val)
                l2 = l2.next
            output_add = output_add.next
        if not l1:
            output_add.next = l2
        else:
            output_add.next = l1
        return output.next
        
# @lc code=end

