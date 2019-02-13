"""
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""

from collections import deque

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""


class Solution:

    def levelOrder(self, root: 'Node') -> 'List[List[int]]':
        if not root:
            return []
        result = []
        queue = deque()
        queue.append([root, 0])
        while queue:
            node, level = queue.popleft()
            if len(result) == level:
                result.append([node.val])
            else:
                result[level].append(node.val)
            if node.children:
                for child in node.children:
                    queue.append([child, level + 1])
        return result
