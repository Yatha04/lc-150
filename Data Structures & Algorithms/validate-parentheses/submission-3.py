class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {'}': '{', ']': '[', ')': '('}
        for i in s:
            if i not in brackets:
                stack.append(i)
            elif i in brackets:
                if (len(stack) > 0):
                    if stack[-1] == brackets[i]:
                        print(stack[-1])
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        if len(stack) > 0:
            return False
        else:
            return True