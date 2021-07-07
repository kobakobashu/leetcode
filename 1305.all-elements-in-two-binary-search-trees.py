#
# @lc app=leetcode id=1305 lang=python3
#
# [1305] All Elements in Two Binary Search Trees
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def getElements(root: TreeNode, elements: List[int]) -> List[int]:

            stack = deque([root])
            while stack:
                curr_node = stack.pop()
                if curr_node is None:
                    continue
                elements.append(curr_node.val)
                stack.append(curr_node.left)
                stack.append(curr_node.right)
            return elements
        
        elements = getElements(root1, [])
        elements = getElements(root2, elements)
        return sorted(elements)
# @lc code=end
