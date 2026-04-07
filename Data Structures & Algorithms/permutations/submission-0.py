class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        set_num = set(nums)
        print(set_num)

        def bt():
            if len(cur) == n:
                # add
                print(f'add cur: {cur}')
                res.append(cur.copy())
                return

            tmp_set = set_num - set(cur)
            print(f'{set_num} {set(cur)} {tmp_set}')
            for i in tmp_set:
                cur.append(i)
                bt()
                cur.pop()

        bt()
        return res

