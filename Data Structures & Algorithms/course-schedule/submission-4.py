class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mapCourse = [[] for _ in range(numCourses)]
        for crse,req in prerequisites:
            mapCourse[crse].append(req)
        visited = set()
        def dfs(course):
            if course in visited:
                return False
            if mapCourse[course] == []:
                return True
            visited.add(course)
            for child in mapCourse[course]:
                if not dfs(child):
                    return False
            visited.remove(course)
            mapCourse[course] = []

            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True