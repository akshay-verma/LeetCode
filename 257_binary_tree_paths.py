"""
Problem 257: Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def findPath(self, root, path, finalPath):
        if root.left is None and root.right is None:
            finalPath.append(path + "{}".format(root.val))
        if root.left:
            self.findPath(root.left, path + "{}->".format(root.val), finalPath)
        if root.right:
            self.findPath(root.right, path + "{}->".format(root.val), finalPath)

    def binaryTreePaths(self, root: 'TreeNode') -> 'List[str]':
        path = ""
        finalPath = []
        if root:
            self.findPath(root, path, finalPath)
        return finalPath
