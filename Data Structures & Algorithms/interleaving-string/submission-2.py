class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m, l = len(s1), len(s2), len(s3)
        if n + m != l:
            return False
        dp = {}

        def dfs(i, j):
            if i == n and j == m:
                return True

            if (i, j) in dp:
                return dp[(i, j)]

            dp[(i, j)] = (
                (dfs(i + 1, j) if i < n and s1[i] == s3[i + j] else False)
                or
                (dfs(i, j + 1) if j < m and s2[j] == s3[i + j] else False)
            )
                
            return dp[(i, j)]
        
        return dfs(0, 0)