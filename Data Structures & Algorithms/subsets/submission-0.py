class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)
        def backtrack(index, path):

            if index == n:
                result.append(path[:])
                return 
            
            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

            backtrack(index + 1, path)

        backtrack(0, [])
        return result