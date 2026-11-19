class Solution:
    
    def tribonacci(self, n: int) -> int:
        dp = {}

        def dfs(n) -> int:
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1
            if n in dp:
                return dp[n]
            
            dp[n] = dfs(n - 3) + dfs(n - 2) + dfs(n - 1)
            return dp[n]
        
        return dfs(n)