class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        temp = [[] for _ in range(n)]
        res = 0
        for x,y in edges:
            temp[x].append(y)
            temp[y].append(x)
        visited = [False] * n

        def dfs(i):
            for nei in temp[i]:
                if not visited[nei]:
                    visited[nei] = True
                    dfs(nei)
            return
        
        for i in range(n):
            if not visited[i]:
                visited[i] = True
                res +=1
                dfs(i)
        return res