"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findDiameter(self, root):
        if root is None:
            return 0
        L = self.findDiameter(root.left)
        R = self.findDiameter(root.right)
        self.result = max(self.result, L + R)
        return max(L, R) + 1

    def diameterOfBinaryTree(self, root) -> int:
        if not root or (root.left is None and root.right is None):
            return 0
        self.result = 0
        self.findDiameter(root)
        return self.result
