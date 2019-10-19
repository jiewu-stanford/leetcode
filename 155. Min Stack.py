'''
Title     : 155. Min Stack
Problem   : https://leetcode.com/problems/min-stack/
'''
'''
use a 2-tuple to store the current element and the min
Reference: https://leetcode.com/problems/min-stack/discuss/49183/Python-one-stack-solution-without-linklist
'''
class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(self.getMin(), x)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1][0]
        else:
            return None

    def getMin(self) -> int:
        if self.stack:
            return self.stack[-1][1]
        else:
            return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()