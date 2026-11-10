class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        seen = [[False] * c for _ in range(r)]
        def dfs(i: int, j: int) -> int:
            if i < 0 or i == r or j < 0 or j == c or seen[i][j] == True or grid[i][j] == 0:
                return 0
            seen[i][j] = True
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        res = 0
        for i in range(r):
            for j in range(c):
                if seen[i][j] == False or grid[i][j] != 0:
                    res = max(res, dfs(i, j))
        
        return res


        