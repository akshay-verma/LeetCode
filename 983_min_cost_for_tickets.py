"""
Solution for Problem 983:
https://leetcode.com/problems/minimum-cost-for-tickets/
"""
import unittest

from collections import deque


class Solution:

    def mincostTickets(self, days: 'List[int]', costs: 'List[int]') -> 'int':
        """
        This will take O(n) time
        """
        cost = 0
        weeklyPass = deque()
        monthlyPass = deque()
        for day in days:
            while weeklyPass and weeklyPass[0][0] + 7 <= day:
                weeklyPass.popleft()
            while monthlyPass and monthlyPass[0][0] + 30 <= day:
                monthlyPass.popleft()
            weeklyPass.append((day, cost + costs[1]))
            monthlyPass.append((day, cost + costs[2]))
            cost = min(cost + costs[0], weeklyPass[0][1], monthlyPass[0][1])
        return cost


class UnitTest(unittest.TestCase):

    def test1(self):
        days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
        costs = [2, 7, 15]
        self.assertEqual(Solution().mincostTickets(days, costs), 17)

    def test2(self):
        days = [1, 4, 6, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21, 22, 23, 27, 28]
        costs = [3, 13, 45]
        self.assertEqual(Solution().mincostTickets(days, costs), 44)

    def test3(self):
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        self.assertEqual(Solution().mincostTickets(days, costs), 11)


if __name__ == "__main__":
    unittest.main(verbosity=2)
