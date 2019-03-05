"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
"""


class Solution:

    def maxProduct(self, nums: 'List[int]') -> int:
        if not nums:
            return 0
        currMax = globalMax = negMax = nums[0]
        for num in nums[1:]:
            newCurrMax = max(currMax * num, negMax * num, num)
            newNegMax = min(currMax * num, negMax * num, num)
            globalMax = max(newCurrMax, newNegMax, globalMax)
            currMax = newCurrMax
            negMax = newNegMax
        return globalMax
