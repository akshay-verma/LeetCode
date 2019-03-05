"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""


class Solution:

    def maxProfit(self, prices: 'List[int]') -> int:
        if not prices:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            sell = prices[i]
            currProfit = max(0, sell - buy)
            if currProfit > profit:
                profit = currProfit
            buy = min(prices[i], buy)
        return profit
