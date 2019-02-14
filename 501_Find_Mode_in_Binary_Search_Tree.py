"""
501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def dfs(self, root, mode):
        if root:
            if root.val in mode:
                mode[root.val] += 1
            else:
                mode[root.val] = 1
        if root.left:
            self.dfs(root.left, mode)
        if root.right:
            self.dfs(root.right, mode)

    def findMode(self, root: 'TreeNode') -> 'List[int]':
        if not root:
            return []
        mode = {}
        self.dfs(root, mode)
        maxVal = None
        result = []
        for key, val in mode.items():
            if not maxVal or val > maxVal:
                maxVal = val
                result = [key]
            elif val == maxVal:
                result.append(key)
        return result
