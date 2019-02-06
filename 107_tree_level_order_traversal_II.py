"""
Problem 107:
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


from collections import deque


class Solution:

    def levelOrderBottom(self, root: 'TreeNode') -> 'List[List[int]]':
        if not root:
            return []
        result = deque()
        rootList = [root]
        while rootList:
            temp = []
            result.append(rootList)
            for root in rootList:
                if root.left:
                    temp.append(root.left)
                if root.right:
                    temp.append(root.right)
            rootList = temp
        final = []
        while result:
            temp = []
            res = result.pop()
            for x in res:
                temp.append(x.val)
            final.append(temp)
        return final
