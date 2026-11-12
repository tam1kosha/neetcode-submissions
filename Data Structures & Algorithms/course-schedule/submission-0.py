class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            preMap[course].append(prereq)
            
        seen = set()
        def dfs(course) -> bool:
            if preMap[course] == []:
                return True
            if course in seen:
                return False

            seen.add(course)
            for prereq in preMap[course]:
                if not dfs(prereq):
                    return False
            seen.remove(course)
            preMap[course] = []
            return True    
        
        for course in preMap:
            if not dfs(course):
                return False
        return True