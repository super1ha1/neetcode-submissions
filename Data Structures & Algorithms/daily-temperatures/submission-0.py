class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for index, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                top_index = stack.pop()
                res[top_index] = index - top_index
            
            stack.append(index)
            print(f'index: {index} t: {t} stack: {stack} res: {res}')
        
        return res
