class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        n = len(nums)
        def dfs(curr, i) -> int:
            if (curr, i) in dp:
                return dp[(curr, i)]
            if i == n:
                if curr == target:
                    return 1
                else:
                    return 0
            dp[(curr, i)] = dfs(curr + nums[i], i + 1) + dfs(curr - nums[i], i + 1)
            return dp[(curr, i)]

        return dfs(0, 0)
