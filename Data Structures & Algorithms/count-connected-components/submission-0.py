class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        neighbors = {i : [] for i in range(n)}

        for n1, n2 in edges:
            neighbors[n1].append(n2)
            neighbors[n2].append(n1)

        count = 0
        visited = set()
        def dfs(curr) -> None:
            if curr in visited:
                return
            visited.add(curr)
            for neighbor in neighbors[curr]:
                dfs(neighbor)
        count = 0
        for i in range(n):
            if not i in visited:
                count += 1
                dfs(i)
        return count            
