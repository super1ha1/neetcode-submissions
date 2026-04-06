class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(total, cur):
            if total < 0:
                return
            if total == 0:
                # accept
                if sorted(cur) not in res:
                    res.append(list(sorted(cur)))
                return

            for n in nums:
                cur.append(n)
                dfs(total - n, cur)
                cur.remove(n)
        
        dfs(target, [])
        
        return res