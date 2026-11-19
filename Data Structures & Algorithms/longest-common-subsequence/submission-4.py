class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        # dp = {}

        # def dfs(i, j) -> int:
        #     if i == n or j == m:
        #         return 0
        #     if (i, j) in dp:
        #         return dp[(i, j)]
            
        #     if text1[i] == text2[j]:
        #         dp[(i, j)] = 1 + dfs(i + 1, j + 1)
        #     else:
        #         dp[(i, j)] = max(dfs(i + 1, j), dfs(i, j + 1))
                
        #     return dp[(i, j)]
        
        # return dfs(0, 0)


        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
        return dp[0][0]



        