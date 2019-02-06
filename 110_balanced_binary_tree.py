"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def isBalanced(self, root: 'TreeNode') -> 'bool':

        def depth(root, result):
            if not root:
                return 0
            L = depth(root.left, result)
            R = depth(root.right, result)
            if abs(L - R) > 1:
                if not result:
                    result.append(False)
            return max(L, R) + 1
        result = []
        depth(root, result)
        return result[0] if result else True
