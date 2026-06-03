class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {']' : '[', '}' : '{', ')': '('}
        stack = []

        for i in s:
            if i not in charMap:
                stack.append(i)
                print(stack)
            else:
                if not stack or charMap[i] != stack[-1]:
                    return False
                stack.pop()
        return (len(stack) == 0)
