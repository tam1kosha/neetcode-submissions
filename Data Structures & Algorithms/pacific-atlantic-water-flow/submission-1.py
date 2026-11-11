class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        seen = {}
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, prev) -> tuple[bool, bool]:
            if (r < 0 or c < 0) and (r == rows or c == cols):
                return True, True
            if (r < 0 or c < 0) and not (r == rows or c == cols):
                return True, False
            if not (r < 0 or c < 0) and (r == rows or c == cols):
                return False, True
            if heights[r][c] > prev:
                return False, False
            if (r, c) in seen:
                return seen[(r, c)]

            seen[(r, c)] = (False, False)      # mark before recursing
            pac, atl = False, False
            for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                p, a = dfs(r + dr, c + dc, heights[r][c])
                pac, atl = pac or p, atl or a  # combine each flag separately
            seen[(r, c)] = (pac, atl)
            return seen[(r, c)]

        for i in range(rows):
            for j in range(cols):
                seen.clear()                   # fresh visited set per start
                p, a = dfs(i, j, float("inf"))
                if p and a:
                    res.append([i, j])
        return res