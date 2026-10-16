class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        temp = [[] for _ in range(n)]
        for x,y in edges:
            temp[x].append(y)
            temp[y].append(x)
        visited = [False] * n
        def dfs(i):
            for child in temp[i]:
                if not visited[child]:
                    visited[child] = True
                    dfs(child)
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                dfs(i)
                res+=1
        return res