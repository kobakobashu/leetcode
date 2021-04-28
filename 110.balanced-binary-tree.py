#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        node_left = self.depth(root.left)
        node_right = self.depth(root.right)
        return (abs(node_left - node_right) < 2) and self.isBalanced(root.left) and self.isBalanced(root.right)
    def depth(self, node):
        if not node:
            return 0
        return max(self.depth(node.left), self.depth(node.right))+1
# @lc code=end

