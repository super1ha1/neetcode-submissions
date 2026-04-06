class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, total, cur):
            if total < 0 or total > target or i < 0 or i >= len(nums):
                return

            if total == target:
                # accept
                res.append(list(cur))
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                # include
                cur.append(nums[j])
                dfs(j, total + nums[j], cur)
                cur.pop()

                # not include
                # dfs(j + 1, total, cur)
        
        dfs(0, 0, [])
        
        return res