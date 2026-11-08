class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        n = len(digits)
        if n == 0:
            return []
        res = []
        path = []
        letters = {}
        letters["2"] = "abc"
        letters["3"] = "def"
        letters["4"] = "ghi"
        letters["5"] = "jkl"
        letters["6"] = "mno"
        letters["7"] = "pqrs"
        letters["8"] = "tuv"
        letters["9"] = "wxyz"

        def dfs(order: int):
            if order == n:
                res.append("".join(path))
                return

            for ch in letters[digits[order]]:
                path.append(ch)
                dfs(order + 1)
                path.pop()
        
        dfs(0)
        return res

        
