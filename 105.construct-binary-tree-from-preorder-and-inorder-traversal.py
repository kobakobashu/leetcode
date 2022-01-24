#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """Function to build tree
        Args:
            preorder(List[int]): preorder traversal of the tree
            inorder(List[int]): inorder traversal of the tree
        Returns:
            Optional[TreeNode]: TreeNode
        """
        if not preorder or not inorder:
            return None

        idx = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        node.left = self.buildTree(preorder[1: 1 + idx], inorder[: idx])
        node.right = self.buildTree(preorder[1 + idx:], inorder[1 + idx:])
        return node
# @lc code=end
