#
# @lc app=leetcode id=1382 lang=python3
#
# [1382] Balance a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        arr = []
        self.inorder(root, arr)
        root = self.construct(arr, 0, len(arr) - 1)
        return root
        
    def inorder(self, root, arr):
        if not root:
            return
        self.inorder(root.left, arr)
        arr.append(root.val)
        self.inorder(root.right, arr)
    
    def construct(self, arr, start, end):
        if start > end:
            return None
        mid = start + (end - start) // 2
        node = TreeNode(arr[mid])
        node.left = self.construct(arr, start, mid - 1)
        node.right = self.construct(arr, mid + 1, end)
        return node
# @lc code=end
