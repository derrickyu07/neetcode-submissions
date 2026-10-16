class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        temp = [[] for _ in range(n)]
        visited = [False] * n
        for x,y in edges:
            temp[x].append(y)
            temp[y].append(x)
        res = 0 
        def dfs(i):
            for child in temp[i]:
                if not visited[child]:
                    visited[child] = True
                    dfs(child)


        for i in range(n):
            if not visited[i]:
                dfs(i)
                visited[i] = True
                res +=1
        return res