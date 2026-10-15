class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        temp = [[] for _ in range(numCourses)]
        visited = set()
        for x,y in prerequisites:
            temp[x].append(y)
        def dfs(course):
            if course in visited:
                return False
            if temp[course] == []:
                return True
            visited.add(course)
            for i in temp[course]:
                if not dfs(i):
                    return False
            visited.remove(course)
            temp[course] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
            