class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = defaultdict(list)
        for e1, e2 in edges:
            m[e1].append(e2)
            m[e2].append(e1)
        
        visit = set()
        def bt(i):
            if i in visit:
                return 
            
            visit.add(i)
            for n in m[i]:
                bt(n)
            
        res = 0
        for i in range(n):
            if i not in visit:
                res += 1
                bt(i)
        
        return res