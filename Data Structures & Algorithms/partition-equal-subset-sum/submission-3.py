class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        fullSum = sum(nums)
        past = {}
        def dfs(curr, index) -> bool:
            if index == n:
                return False
            if curr == fullSum - curr:
                return True
            if (curr, index) in past:
                return past[(curr, index)]

            include = dfs(curr + nums[index], index + 1)
            exclude = dfs(curr, index + 1)

            past[(curr + nums[index], index + 1)] = include
            past[(curr, index + 1)] = exclude

            return include or exclude

        return dfs(0, 0)
