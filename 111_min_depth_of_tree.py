"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def minDepth(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        L = self.minDepth(root.left)
        R = self.minDepth(root.right)
        if L and R or (not L and not R):
            return min(L, R) + 1
        else:
            return max(L, R) + 1
