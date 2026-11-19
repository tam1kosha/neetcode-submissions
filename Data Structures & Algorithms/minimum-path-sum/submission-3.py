class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m, n = len(grid), len(grid[0])
        def dfs(r, c) -> int:
            if r < 0 or r >= m or c < 0 or c >= n:
                return 201
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if (r, c) in dp:
                return dp[(r, c)]

            res = grid[r][c] + min(
                dfs(r + 1, c),
                dfs(r, c + 1)
            )

            dp[(r, c)] = res
            return res

        return dfs(0, 0)