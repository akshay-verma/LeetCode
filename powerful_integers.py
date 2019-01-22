"""
970. Powerful Integers

Given two non-negative integers x and y, an integer is powerful if it is equal to x^i + y^j
for some integers i >= 0 and j >= 0.

Return a list of all powerful integers that have value less than or equal to bound.

You may return the answer in any order.  In your answer, each value should occur at most once.
"""


class Solution(object):

    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        result = []
        for i in range(0, 10):
            for j in range(0, 10):
                res = x**i + y**j
                if res <= bound and res not in result:
                    result.append(res)
        return result


res = Solution().powerfulIntegers(3, 5, 15)
print(res)
