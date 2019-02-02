"""
Problem 2:
https://leetcode.com/problems/add-two-numbers/
"""

import unittest


class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        startNode = ListNode(None)
        remainder = 0
        tempNode = startNode
        while l1 or l2 or remainder:
            l1Val = l2Val = 0
            if l1:
                l1Val = l1.val
                l1 = l1.next
            if l2:
                l2Val = l2.val
                l2 = l2.next
            res = l1Val + l2Val + remainder
            remainder = 0
            if (res // 10) > 0:
                remainder = 1
            tempNode.next = ListNode(res % 10)
            tempNode = tempNode.next
        return startNode.next


class UnitTest(unittest.TestCase):

    def createNodeList(self, numList):
        startNode = ListNode(numList[0])
        node = startNode
        for index in range(1, len(numList)):
            node.next = ListNode(numList[index])
            node = node.next
        node.next = None
        return startNode

    def assertTestCase(self, answer, result):
        self.assertIsNotNone(result, "Result is None")
        index = 0
        while result:
            self.assertEqual(answer[index], result.val)
            index += 1
            result = result.next

    def test(self):
        list1 = self.createNodeList([2, 4, 3])
        list2 = self.createNodeList([5, 6, 4])
        answer = [7, 0, 8]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)

    def test1(self):
        list1 = self.createNodeList([2, 4, 3])
        list2 = self.createNodeList([5])
        answer = [7, 4, 3]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)

    def test2(self):
        list1 = self.createNodeList([2, 4, 3])
        list2 = self.createNodeList([0, 0, 5])
        answer = [2, 4, 8]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)

    def test3(self):
        list1 = self.createNodeList([5])
        list2 = self.createNodeList([5])
        answer = [0, 1]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)

    def test4(self):
        list1 = self.createNodeList([9, 9, 9])
        list2 = self.createNodeList([9, 9, 9])
        answer = [8, 9, 9, 1]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)

    def test5(self):
        list1 = self.createNodeList([9, 8])
        list2 = self.createNodeList([1])
        answer = [0, 9]
        result = Solution().addTwoNumbers(list1, list2)
        self.assertTestCase(answer, result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
