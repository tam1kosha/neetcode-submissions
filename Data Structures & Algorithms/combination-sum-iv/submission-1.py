class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        
        def dfs(curr) ->int:
            if curr == target:
                return 1
            if curr > target:
                return 0
            if curr in dp:
                return dp[curr]
            res = 0
            for i in range(n):
                res += dfs(curr + nums[i])
            dp[curr] = res
            return res
        
        return dfs(0)
