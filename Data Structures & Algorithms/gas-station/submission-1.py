class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            if gas[i] >= cost[i]:
                start = i
                cur = 0
                while True:
                    cur += gas[start] - cost[start]
                    print(f'i: {i} start: {start} cur: {cur}')
                    if cur < 0:
                        break
                    start += 1
                    if start == n:
                        start = 0
                    
                    if start == i:
                        return i
        
        return -1

                    
        