class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        pos, neg = nums.copy(), nums.copy()
        if n == 1:
            return nums[0]
        res = nums[0]
        pos[0] = nums[0]
        for i in range(1, n):
            neg[i] = min(nums[i], neg[i - 1] * nums[i], pos[i - 1] * nums[i])
            pos[i] = max(nums[i], pos[i - 1] * nums[i], neg[i - 1] * nums[i])
            res = max(res, pos[i])
        
        return res