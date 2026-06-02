class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token in operators:
                op1 = stack.pop()  # right operand
                op2 = stack.pop()  # left operand
                if token == '+':
                    stack.append(op2 + op1)
                elif token == '-':
                    stack.append(op2 - op1)
                elif token == '*':
                    stack.append(op2 * op1)
                else:
                    stack.append(int(op2 / op1))  # truncates toward zero
            else:
                stack.append(int(token))

        return stack[0]