class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        dp = nums.copy()
        dpneg = nums.copy()
        if n == 1:
            return nums[0]
        res = nums[0]
        dp[0] = nums[0]
        for i in range(1, n):
            dpneg[i] = min(nums[i], dpneg[i - 1] * nums[i], dp[i - 1] * nums[i])
            dp[i] = max(nums[i], dp[i - 1] * nums[i], dpneg[i - 1] * nums[i])
            res = max(res, dp[i])
        
        return res