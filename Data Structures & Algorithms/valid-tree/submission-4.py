class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n+ 1:
            return False
        visited = set()
        temp = [[] for _ in range(n)]
        for x,y in edges:
            temp[x].append(y)
            temp[y].append(x)
        def dfs(node,par):

            if node in visited:
                return False
            visited.add(node)
            for child in temp[node]:
                if child == par:
                    continue
                if not dfs(child,node):
                    return False
            return True
        return dfs(0,-1) and len(visited)==n

