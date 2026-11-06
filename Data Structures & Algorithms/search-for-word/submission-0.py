class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #base case 1: current char == last char of word -> true
        #base case 2: current char != any char of word -> backtrack, mark that char as visited
        #base case 3: no more available char around 

        # x, y, index = 0, 0, 0
        ROWS, COLS = len(board), len(board[0])
        path = set()
        n = len(word)
        def backtrack(x, y, index):
            if index == n:
                return True

            if x < 0 or y < 0 or x >= ROWS or y >= COLS or (x, y) in path or board[x][y] != word[index]:
                return False

            path.add((x, y))
            result = (
                backtrack(x + 1, y, index + 1) or
                backtrack(x, y + 1, index + 1) or
                backtrack(x - 1, y, index + 1) or
                backtrack(x, y - 1, index + 1) 
            )  
            path.discard((x, y))
            return result

        for i in range(ROWS):
            for j in range(COLS):
                if backtrack(i, j, 0): return True
        
        return False
        