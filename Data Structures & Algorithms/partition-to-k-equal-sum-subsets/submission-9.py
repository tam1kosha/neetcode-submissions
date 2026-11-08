class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        target = sum(nums) // k
        nums.sort(reverse=True)
        n = len(nums)
        visited = set()
        checked = set()
        def dfs(index, k, subsetSum):
            if k == 0:
                return True
            if subsetSum == target:
                return dfs(0, k - 1, 0)

            for j in range(index, n):
                if j in visited or subsetSum + nums[j] > target or (subsetSum, nums[j]) in checked:
                    continue

                visited.add(j)
                
                result = dfs(j + 1, k, subsetSum + nums[j])

                if result:
                    return True
                else:
                    checked.add((subsetSum, nums[j]))               
                
                visited.remove(j)    

            return False
        
        return dfs(0, k, 0)
            
            
            