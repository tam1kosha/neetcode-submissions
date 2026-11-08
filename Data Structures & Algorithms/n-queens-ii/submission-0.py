class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posd = set()
        negd = set()

        self.count = 0
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                self.count += 1
                return
            
            for c in range(n):
                if c in col or (r + c) in posd or (r - c) in negd:
                    continue
                board[r][c] = "Q"

                col.add(c)
                posd.add(r + c)
                negd.add(r - c)

                backtrack(r + 1)

                col.discard(c)
                posd.discard(r + c)
                negd.discard(r - c)

                board[r][c] = "."
        
        backtrack(0)
        return self.count