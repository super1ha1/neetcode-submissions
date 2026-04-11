class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        m = defaultdict(int)
        for t in tasks:
            m[t] += 1
        
        maxF = max(m.values())
        numMaxF = len({k for k in m.items() if k[1] == maxF})

        # X Y idle X Y idle X Y
        # maxF = 3, numMaxF = 2 => 8
        # 
        res = (maxF - 1) * (n + 1) + numMaxF
        print(len(tasks), res)
        return max(len(tasks), res )


        # max(maxF * numMaxFre )