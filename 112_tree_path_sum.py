"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def hasPathSum(self, root: 'TreeNode', sum: 'int') -> 'bool':
        self.total = 0
        self.sum = sum
        self.result = False

        def calculate(root):
            if root:
                self.total += root.val
            else:
                return 0
            # print(root.val, self.total)
            if root.left is None and root.right is None:
                if self.total == self.sum:
                    self.result = True
            calculate(root.left)
            if root.left:
                self.total -= root.left.val
            calculate(root.right)
            if root.right:
                self.total -= root.right.val
        calculate(root)
        return self.result
