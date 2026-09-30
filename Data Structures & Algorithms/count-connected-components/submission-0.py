class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        eMap = [[] for _ in range(n)]
        for x,y in edges:
            eMap[x].append(y)
            eMap[y].append(x)
        visited = [False] * n

        def dfs(node):
            for child in eMap[node]:
                if not visited[child]:
                    visited[child] = True
                    dfs(child)
        
        res = 0
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                res+=1
                dfs(i)
        return res
