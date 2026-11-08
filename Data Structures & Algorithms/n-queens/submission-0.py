class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posd = set()
        negd = set()

        res = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return
            
            for c in range(n):
                if c in col or (r + c) in posd or (r - c) in negd:
                    continue
                board[r][c] = "Q"

                col.add(c)
                posd.add(r + c)
                negd.add(r - c)

                backtrack(r + 1)

                col.remove(c)
                posd.remove(r + c)
                negd.remove(r - c)

                board[r][c] = "."
        
        backtrack(0)
        return res