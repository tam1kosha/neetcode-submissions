class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        DP = [0] * (amount + 1)
        DP[0] = 1
            
        for i in range(len(coins) - 1, -1, -1):
            nextDP = [0] * (amount + 1)
            nextDP[0] = 1
            for curr in range(1, amount + 1):
                nextDP[curr] = DP[curr]
                if curr - coins[i] >= 0:
                    nextDP[curr] += nextDP[curr - coins[i]]
            DP = nextDP
        return DP[amount]