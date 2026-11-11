class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        q = deque()
        seen = set()
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
                seen.add((r, 0))
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
                seen.add((r, COLS - 1))
            
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
                seen.add((0, c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
                seen.add((ROWS - 1, c))

        def around(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] == "X" or (r, c) in seen:
                return
            q.append((r, c))
            seen.add((r, c))
            
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                around(r, c + 1)
                around(r, c - 1)
                around(r + 1, c)
                around(r - 1, c)

        for i in range(1, ROWS - 1):
            for j in range(1, COLS - 1):
                if board[i][j] == "O" and not (i, j) in seen:
                    board[i][j] = "X"

