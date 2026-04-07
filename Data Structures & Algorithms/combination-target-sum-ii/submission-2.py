class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)

        res = []
        candidates.sort()
        cur = []

        def bt(index, total):
            if total == target:
                # add
                res.append(cur.copy())
                return

            if index < 0 or index >= n or total > target:
                return

            # add cur
            cur.append(candidates[index])
            bt(index + 1, total + candidates[index])
            cur.pop()
            
            # no current    
            while index + 1 < n and candidates[index + 1] == candidates[index]:
                index += 1
            bt(index + 1, total)

        
        bt(0, 0)
        return res
