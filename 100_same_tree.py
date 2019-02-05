# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    def preOrderTraversal(self, root, result):
        if root:
            result.append(root.val)
            if root.left or root.right:
                if root.left:
                    self.preOrderTraversal(root.left, result)
                else:
                    result.append(None)
                if root.right:
                    self.preOrderTraversal(root.right, result)
                else:
                    result.append(None)

    def isSameTree(self, p: 'TreeNode', q: 'TreeNode') -> 'bool':
        res1 = []
        self.preOrderTraversal(p, res1)
        res2 = []
        self.preOrderTraversal(q, res2)
        return res1 == res2
