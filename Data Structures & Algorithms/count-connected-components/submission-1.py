class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        edgeMap = [[] for _ in range(n)]
        for x,y in edges:
            edgeMap[x].append(y)
            edgeMap[y].append(x)
        visited = [False] * n

        def dfs(i):
            for child in edgeMap[i]:
                if not visited[child]:
                    visited[child] = True
                    dfs(child)
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res +=1

        return res