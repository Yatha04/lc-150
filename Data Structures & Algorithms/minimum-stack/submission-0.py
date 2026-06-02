class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        topElement = self.stack[-1]
        return topElement

    def getMin(self) -> int:
        return self.minStack[-1]