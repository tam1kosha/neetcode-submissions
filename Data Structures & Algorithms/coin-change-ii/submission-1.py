class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        cache = {}
        def dfs(i, curr) -> int:
            if curr == 0:
                return 1
            if i == len(coins) or curr < 0:
                return 0
            if (i, curr) in cache:
                return cache[(i, curr)]
            res = dfs(i, curr - coins[i]) + dfs(i + 1, curr)
            cache[(i, curr)] = res
            return res
        return dfs(0, amount)


        