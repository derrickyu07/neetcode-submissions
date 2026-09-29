class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        adj = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            adj[crs].append(pre)

        def dfs(course):
            if course in visited:
                return False
            if adj[course] == []:
                return True
            visited.add(course)
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            visited.remove(course)
            adj[course] = []
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True