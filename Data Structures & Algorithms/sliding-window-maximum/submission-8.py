class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = []
        deq = deque([])
        for i in range(0, k):
            while len(deq) > 0 and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
        ans.append(nums[deq[0]])
        for i in range(k, n):
            if i - deq[0] >= k:
                deq.popleft()
            while len(deq) > 0 and nums[deq[-1]] < nums[i]:
                deq.pop()
            deq.append(i)
            ans.append(nums[deq[0]])
        return ans

            
