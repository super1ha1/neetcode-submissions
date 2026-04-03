class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []

        for i in range(len(nums)):
            if nums[i] > 0:
                continue
            
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    cur = sorted([nums[i] , nums[left], nums[right]])
                    if cur not in res:
                        res.append(cur)
                    left += 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return res
            