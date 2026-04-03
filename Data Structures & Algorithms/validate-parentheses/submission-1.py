class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in ['(', '[', '{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                    
                if c == ']':
                    if stack[-1] != '[':
                        return False
                    else:
                        stack.pop()
                elif c == ')':
                    if stack[-1] != '(':
                        return False
                    else:
                        stack.pop()
                elif c == '}':
                    if stack[-1] != '{':
                        return False
                    else:
                        stack.pop()
                else:
                    pass
        return len(stack) == 0
                            
        