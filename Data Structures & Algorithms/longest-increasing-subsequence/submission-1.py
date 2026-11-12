class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = {0 : 1}

        def dfs(index) ->int:        
            if index in dp:
                return dp[index]
            res = 1
            for i in range(index, -1, -1):
                if nums[i] < nums[index]:
                    res = max(res, 1 + dfs(i))
            dp[index] = res
            return res
        
        ans = 0
        for i in range(len(nums) - 1, -1, -1):
            ans = max(ans, dfs(i))
        
        return ans
            
