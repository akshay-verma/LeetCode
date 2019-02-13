"""
Problem 404: Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findSum(self, root, total):
        if root.left and (root.left.left is None and root.left.right is None):
            total[0] += root.left.val
        if root.left:
            self.findSum(root.left, total)
        if root.right:
            self.findSum(root.right, total)

    def sumOfLeftLeaves(self, root: 'TreeNode') -> 'int':
        if not root:
            return 0
        total = [0]
        self.findSum(root, total)
        return total[0]
