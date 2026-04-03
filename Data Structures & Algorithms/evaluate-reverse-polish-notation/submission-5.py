class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t in ['+', '-', '*', '/']:
                # pop 2, compute, push back
                if len(stack) < 2:
                    raise ValueError('invalid expression')
                t1 = stack.pop()
                t2 = stack.pop()
                c = f'{t2}{t}{t1}'
                t3 = int(eval(c))
                print(c, t3)
                stack.append(t3)
            else:
                stack.append(t)
        
        return int(stack[-1])
        