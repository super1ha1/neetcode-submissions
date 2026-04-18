class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        cur = []
        n = len(nums)
        nums.sort()

        def dfs(index):
            if index == n:
                res.append(cur.copy())
                return
            
            # 2 options, add or skip
            # add
            cur.append(nums[index])
            dfs(index + 1)
            cur.pop()

            # skip
            while index < n - 1 and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1)
        
        dfs(0)

        return res