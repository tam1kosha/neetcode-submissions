class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
        path = []
        visiting = set()
        visited = set()
        def dfs(course) -> bool:
            if course in visiting:
                return False
            if course in visited:
                return True
            
            visiting.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            visiting.remove(course)
            visited.add(course)
            path.append(course)
            return True

        for course in range(numCourses):
            if dfs(course) == False:    
                return []
        return path



        