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

    def preOrderTraversalRight(self, root, result):
        if root:
            result.append(root.val)
            if root.left or root.right:
                if root.right:
                    self.preOrderTraversalRight(root.right, result)
                else:
                    result.append(None)
                if root.left:
                    self.preOrderTraversalRight(root.left, result)
                else:
                    result.append(None)

    def checkNodes(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val == q.val:
            left = self.checkNodes(p.left, q.right)
            right = self.checkNodes(p.right, q.left)
            return left and right
        else:
            return False

    def isSymmetric(self, root: 'TreeNode') -> 'bool':
        if not root:
            return True
        # Solution 1
        # leftSubTree = []
        # self.preOrderTraversal(root.left, leftSubTree)
        # rightSubTree = []
        # self.preOrderTraversalRight(root.right, rightSubTree)
        # return leftSubTree == rightSubTree

        # Solution 2
        return self.checkNodes(root.left, root.right)
