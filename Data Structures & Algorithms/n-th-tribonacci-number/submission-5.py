class Solution:
    
    def tribonacci(self, n: int) -> int:
        # dfs + memoization solution
        # dp = {}

        # def dfs(n) -> int:
        #     if n == 0:
        #         return 0
        #     if n == 1 or n == 2:
        #         return 1
        #     if n in dp:
        #         return dp[n]
            
        #     dp[n] = dfs(n - 3) + dfs(n - 2) + dfs(n - 1)
        #     return dp[n]
        
        # return dfs(n)
        # dp solution
        # if n <= 2:
        #     if n == 0:
        #         return 0
        #     else:
        #         return 1
        # dp = [0 for _ in range(n + 1)]
        # dp[0] = 0
        # dp[1] = dp[2] = 1
        # for i in range(3, n + 1):
        #     dp[i] = dp[i - 3] + dp[i - 2] + dp[i - 1]
        # return dp[n]
        # dp solution with optimized space complexity from O(n) to O(1)
            if n <= 2:
                if n == 0:
                    return 0
                else:
                    return 1
            first, second, third = 0, 1, 1

            for i in range(3, n + 1):
                curr = (first + second + third)
                first = second
                second = third
                third = curr
            return third
