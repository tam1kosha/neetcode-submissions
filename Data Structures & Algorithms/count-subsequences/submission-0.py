class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        t_len = len(t)
        s_len = len(s)

        dp = {}

        def dfs(i, j) -> int:
            if j == t_len:
                return 1
            if i == s_len:
                return 0

            if (i, j) in dp:
                return dp[(i, j)]
            
            res = dfs(i + 1, j)        
            if s[i] == t[j]:
                res += dfs(i + 1, j + 1) 
            dp[(i, j)] = res
            return res
                
                        
        return dfs(0, 0)