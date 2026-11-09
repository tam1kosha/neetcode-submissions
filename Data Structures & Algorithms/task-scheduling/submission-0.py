class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        i imagine that we could put all tasks to priority queue based on their frequencies, in ascending order. we want to output min number of cycles, and that is possible if we try to avoid idle condition of cpu, hence we should target building sequences of tasks without  
        """
        
        count = Counter(tasks)
        maxHeap = [c for c in count.values()]
        heapq.heapify_max(maxHeap)

        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if maxHeap:
                curr = heapq.heappop_max(maxHeap) - 1
                if curr:
                    q.append([curr, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush_max(maxHeap, q.popleft()[0])
        return time

