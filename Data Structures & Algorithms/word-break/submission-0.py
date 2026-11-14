class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        if s in wordDict:
            return True

        dp = {}
        def dfs(index):
            if index == n:
                return True
            if index in dp:
                return dp[index]
            for i in range(index + 1, n + 1):
                if s[index : i] in wordDict and dfs(i):
                    return True
            
            dp[index] = False
            return False

            
        
        return dfs(0)