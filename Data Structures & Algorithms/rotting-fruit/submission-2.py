class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])


        q = deque()
        seen = set()

        def addRott(r, c):
            if r < 0 or r >= row or c < 0 or c >= col or (r, c) in seen or grid[r][c] == 0 or grid[r][c] == 2:
                return
            grid[r][c] = 2
            q.append((r, c))
            seen.add((r, c)) 
        fresh = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
                    seen.add((i, j))
        if fresh == 0: return 0

        minutes = -1
        while q:

            for i in range(len(q)):
                r, c = q.popleft()
                
                addRott(r, c + 1)
                addRott(r, c - 1)
                addRott(r + 1, c)
                addRott(r - 1, c)
                
            minutes += 1

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return minutes

        