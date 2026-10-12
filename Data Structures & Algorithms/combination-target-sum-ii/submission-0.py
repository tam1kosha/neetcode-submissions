class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        def backtrack(path, index, curr):
            print(path)
            if curr == target:
                result.append(path[:])
                return

            if index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if curr + candidates[i] > target:
                    break
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                path.append(candidates[i])
                backtrack(path, i + 1, curr + candidates[i])
                path.pop()

        backtrack([], 0, 0)
        return result
        
                
            
            