"""
538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def convert(self, root, total):
        if not root:
            return total
        total = self.convert(root.right, total)
        total += root.val
        root.val = total
        total = self.convert(root.left, total)
        return total

    def convertBST(self, root: 'TreeNode') -> 'TreeNode':
        self.convert(root, 0)
        return root
