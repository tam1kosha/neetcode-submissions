class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def backtrack(curr, last, path):
            if curr == target:
                result.append(path[:])
                return
            
            for num in nums:
                if curr + num > target or num < last:
                    continue
                path.append(num)
                backtrack(curr + num, num, path)
                path.pop()

        backtrack(0, 1, [])
        return result
            

        
