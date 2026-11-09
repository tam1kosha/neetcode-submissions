class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == "0" or (i, j) in visited:
                return
            if grid[i][j] == "1":
                visited.add((i, j))
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if (i, j) in visited or grid[i][j] == "0":
                    continue

                dfs(i, j)
                
                count += 1
                

        return count