class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(prev, i, j) -> int:
            if i < 0 or j < 0 or i == ROWS  or j == COLS or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 1 + max(
                dfs(matrix[i][j], i + 1, j),
                dfs(matrix[i][j], i - 1, j),
                dfs(matrix[i][j], i, j + 1),
                dfs(matrix[i][j], i, j - 1)
            )
            return dp[(i, j)]
        ans = 0
        for i in range(ROWS):
            for j in range(COLS):
               ans = max(ans, dfs(-1, i, j))
        return ans 
            
