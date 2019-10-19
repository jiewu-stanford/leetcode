'''
Title     : 232. Implement Queue using Stacks
Problem   : https://leetcode.com/problems/implement-queue-using-stacks/
'''
'''
a queue can be simulated using two stack, the only difficulty is the push() operation which requires the use of auxiliary stack
Reference: https://leetcode.com/problems/implement-queue-using-stacks/discuss/64198/Share-my-python-solution-(32ms)
'''
class MyQueue:

    def __init__(self):
        self.mainStack = []
        self.auxStack = []

    def push(self, x: int) -> None:
        while self.mainStack:
            self.auxStack.append(self.mainStack.pop())
        self.mainStack.append(x)
        while self.auxStack:
            self.mainStack.append(self.auxStack.pop())

    def pop(self) -> int:
        return self.mainStack.pop()

    def peek(self) -> int:
        return self.mainStack[-1]

    def empty(self) -> bool:
        return not self.mainStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()