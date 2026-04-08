class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)

        def bt(index):
            print(f'bt: {index} {cur}')
            if index == n:
                # add
                res.append(list(cur))
                print(f'add {cur}')
                return
            

            bt(index + 1)

            cur.append(nums[index])
            bt(index + 1)
            cur.pop()
        
        
        bt(0)

        return res



        