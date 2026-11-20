class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0] * (k + 1)
        for pile in piles:
            for c in range(k, 0, -1):
                total = 0
                for j in range(min(c, len(pile))):
                    total += pile[j]
                    dp[c] = max(dp[c], dp[c - j - 1] + total)
        return dp[k]
