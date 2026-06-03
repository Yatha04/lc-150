class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        oppMap = {'+', '-', '*', '/'}
        
        for i in tokens:
            if i not in oppMap:
                stack.append(int(i))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                if i == '+':
                    stack.append(int(op1) + int(op2))
                elif i == '-':
                    stack.append(int(op1) - int(op2))
                elif i == '*':
                    stack.append(int(op1) * int(op2))
                else:
                    stack.append(int(int(op1) / int(op2)))
        return stack[-1]
