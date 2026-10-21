class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        l = 1
        r = max(piles)
        res = r
        while l <= r:
            m = (l + r) // 2

            hours = 0
            
            for i in range(0, n):
                hours += math.ceil(piles[i] / m)
            
            if hours > h:
                l = m + 1
            else:
                res = min(res, m)
                r = m - 1
            
        return res