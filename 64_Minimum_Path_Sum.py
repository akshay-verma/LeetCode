"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/
"""


class Solution:

    def minPathSum(self, grid: "List[List[int]]") -> int:
        row = len(grid)
        col = len(grid[0])
        # Update first column
        for i in range(1, col):
            grid[0][i] += grid[0][i - 1]
        # Update first row
        for j in range(1, row):
            grid[j][0] += grid[j - 1][0]
        # Backtrack: For each value, check the minimum of path coming from its left and up
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]
        return grid[row - 1][col - 1]


if __name__ == "__main__":
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    res = Solution().minPathSum(grid)
    print(res)
