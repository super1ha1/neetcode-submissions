class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = defaultdict(list)
        for p1, p2 in prerequisites:
            m[p1].append(p2)
        print(m)

        visit = [0] * numCourses

        res = []
        
        def bt(i):
            if visit[i] == -1:
                res.append(i)
                return

            if visit[i] == 1:
                return
            
            visit[i] = -1
            for n in m[i]:
                bt(n)
            
            visit[i] = 1
        
        for i in range(numCourses):
            bt(i)
        
        return len(res) == 0

        