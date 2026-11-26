class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        filtered = []
        for ai, bi, ci in triplets:
            if ai > target[0] or bi > target[1] or ci > target[2]:
                continue
            filtered.append((ai, bi, ci))
        
        myset = set()
        for ai, bi, ci in filtered:
            
            if (ai, 0) not in myset and ai == target[0]:
                
                myset.add((ai, 0))
            if (bi, 1) not in myset and bi == target[1]:
               
                myset.add((bi, 1))
            if (ci, 2) not in myset and ci == target[2]:
                
                myset.add((ci, 2))
            
        
        return True if len(myset) == 3 else False
