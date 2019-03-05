"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""

import unittest


class Solution:

    def maxSumSubarray(self, array):
        currMax = globalMax = array[0]
        start = end = 0
        for i in range(1, len(array)):
            num = array[i]
            if currMax < 0:
                start = i
            currMax = max(num, currMax + num)
            if currMax >= globalMax:
                globalMax = currMax
                end = i
        # To get start and end index of maximum sum subarray
        # return start, end, globalMax
        return globalMax


class UnitTest(unittest.TestCase):

    def test1(self):
        array = [1, 5, -1, 0, 10]
        res = Solution().maxSumSubarray(array)
        answer = 15
        self.assertEqual(res, answer)

    def test2(self):
        array = [0, -1, -5, 0, -4]
        res = Solution().maxSumSubarray(array)
        answer = 0
        self.assertEqual(res, answer)

    def test3(self):
        array = [1, 2, -3, 4, 6]
        res = Solution().maxSumSubarray(array)
        answer = 10
        self.assertEqual(res, answer)


if __name__ == "__main__":
    unittest.main(verbosity=2)
