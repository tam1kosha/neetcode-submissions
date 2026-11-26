class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        # dp = {}
        # def dfs(l, r) -> int:
        #     if l > r:
        #         return 0
        #     if (l, r) in dp:
        #         return dp[(l, r)]
            
        #     dp[(l, r)] = 0
        #     for i in range(l, r + 1):
        #         coins = nums[l - 1] * nums[i] * nums[r + 1]
        #         coins += dfs(l, i - 1) + dfs(i + 1, r)
        #         dp[(l, r)] = max(dp[(l, r)], coins)
            
        #     return dp[(l, r)]
        
        # return dfs(1, n - 2)

        dp = [[0 for _ in range(n)] for _ in range(n)]
        for l in range(n - 2, 0, -1):         
            for r in range(l, n - 1):          
                for i in range(l, r + 1):  
                    coins = nums[l - 1] * nums[i] * nums[r + 1]
                    coins += dp[l][i - 1] + dp[i + 1][r]
                    dp[l][r] = max(dp[l][r], coins)

        return dp[1][n - 2]              
                
