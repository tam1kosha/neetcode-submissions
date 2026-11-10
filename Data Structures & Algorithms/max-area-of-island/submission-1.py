class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        seen = set()
        def dfs(i, j) -> int:
            if i < 0 or i == r or j < 0 or j == c or (i, j) in seen or grid[i][j] == 0:
                return 0
            seen.add((i, j))
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        res = 0
        for i in range(r):
            for j in range(c):
                if not (i, j) in seen or grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        
        return res


        