"""
62. Unique Paths
https://leetcode.com/problems/unique-paths/
"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * n] * m
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]


if __name__ == "__main__":
    res = Solution().uniquePaths(4, 4)
    print(res)
