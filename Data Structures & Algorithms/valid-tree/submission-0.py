class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = defaultdict(list)
        for e1, e2 in edges:
            m[e1].append(e2)
            m[e2].append(e1)
        
        visit = [0] * n
        has_cycle = []

        def dfs(node, parent):
            if visit[node] == 1:
                return
            
            if visit[node] == -1:
                has_cycle.append(node)
                return
            
            visit[node] = -1
            for nei in m[node]:
                if nei == parent:
                    # just parent, skip
                    continue
                else:
                    dfs(nei, node)
            
            visit[node] = 1
        
        res = 0
        for i in range(n):
            if visit[i] == 0:
                res += 1
                dfs(i, -1)
        
        print(res)
        print(f'has_cycle: {has_cycle}')
        print(visit)
        return res == 1 and len(has_cycle) == 0
            

        