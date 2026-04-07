class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        cur = []
        n = len(nums)
        # set_num = set(nums)
        visit = [0] * n
        # print(set_num)

        def bt():
            if len(cur) == n:
                # add
                # print(f'add cur: {cur}')
                res.append(cur.copy())
                return

            # tmp_set = set_num - set(cur)
            # print(f'{set_num} {set(cur)} {tmp_set}')
            for i in range(n):
                if visit[i] == 1:
                    continue

                cur.append(nums[i])
                visit[i] = 1
                
                bt()

                cur.pop()
                visit[i] = 0

        bt()
        return res

