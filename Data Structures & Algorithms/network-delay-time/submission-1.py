class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = {i : [] for i in range(1, n + 1)}

        for u, v, w in times:
            edges[u].append((w, v))
        
        minHeap = [(0, k)]
        seen = set()
        t = 0
        while minHeap:
            weight1, node1 = heapq.heappop(minHeap)
            if node1 in seen:
                continue
            seen.add(node1)
            t = weight1

            for weight2, node2 in edges[node1]:
                if node2 not in seen:
                    heapq.heappush(minHeap, (weight1 + weight2, node2))


        return t if len(seen) == n else -1  



