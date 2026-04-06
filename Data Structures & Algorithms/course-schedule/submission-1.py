class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for p1, p2 in prerequisites:
            m[p1].append(p2)
        print(m)

        visit = set()
        visiting = set()

        res = [0]
        
        def bt(i):
            if i in visiting:
                res[0] = 1
                return
            if i in visit:
                return
           
            visiting.add(i)
            for n in m[i]:
                bt(n)
            
            # finish, remove visisting
            visiting.remove(i)
            visit.add(i)
        
        for i in range(numCourses):
            bt(i)
        
        return res[0] == 0

        