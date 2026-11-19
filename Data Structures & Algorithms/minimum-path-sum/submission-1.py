class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = {}
        m, n = len(grid), len(grid[0])
        visited = set()
        def dfs(r, c) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited:
                return 1000000000000
            if r == m - 1 and c == n - 1:
                return grid[r][c]
            if (r, c) in dp:
                return dp[(r, c)]

            visited.add((r, c))
            res = grid[r][c] + min(
                dfs(r + 1, c),
                dfs(r, c + 1)
            )
            visited.remove((r, c))

            dp[(r, c)] = res
            return res

        return dfs(0, 0)