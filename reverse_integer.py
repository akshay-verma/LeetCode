"""
https://leetcode.com/problems/reverse-integer/
"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        new = 0
        rangeOfVal = 2**31
        oldX = x
        if x < 0:
            x = abs(x)
        while(x != 0):
            mod = x % 10
            new = new * 10 + mod
            x = x // 10
            print(mod, new, x)
            if new >= (rangeOfVal - 1) or new <= -(rangeOfVal):
                return 0
        if oldX < 0:
            return -new
        return new


print(Solution().reverse(-2**20))
