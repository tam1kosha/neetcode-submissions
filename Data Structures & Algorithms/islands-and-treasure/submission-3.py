class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        row = len(grid)
        col = len(grid[0])

        q = deque()
        seen = [[False for _ in range(col)] for _ in range(row)] 

        def addIsland(r, c):
            if r < 0 or r == row or c < 0 or c == col or grid[r][c] == -1 or seen[r][c] == True:
                return
            q.append((r, c))
            seen[r][c] = True

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    q.append((i, j))
                    seen[i][j] = True
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                seen[r][c] = True
                addIsland(r, c + 1)
                addIsland(r, c - 1)
                addIsland(r + 1, c)
                addIsland(r - 1, c)
            
            dist += 1
        
