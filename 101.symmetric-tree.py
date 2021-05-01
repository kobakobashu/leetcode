#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        """
        time: O(N)  N : the number of all nodes
        space: O(N)
        """
        if not root:
            return True
        else:
            return self.isMirror(root.left, root.right)
            
    def isMirror(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val == right.val:
            outtree = self.isMirror(left.left, right.right)
            intree = self.isMirror(left.right, right.left)
            return outtree and intree
        return False


# @lc code=end

