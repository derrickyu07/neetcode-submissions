class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        crseMap = [[] for _ in range(numCourses)]
        for x,y in prerequisites:
            crseMap[x].append(y)
        visited = set()

        def dfs(course):
            if course in visited:
                return False
            if crseMap[course] == []:
                return True
            visited.add(course)
            for pre in crseMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            crseMap[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True