'''
Title     : 225. Implement Stack using Queues
Problem   : https://leetcode.com/problems/implement-stack-using-queues/
'''
'''
the only difficulty is the push() operation which requires reversing the order using successive popleft() and append(), which however is still faster than .appendleft()
Reference: https://leetcode.com/problems/implement-stack-using-queues/discuss/62516/Concise-1-Queue-Java-C%2B%2B-Python
'''
import collections
class MyStack:

    def __init__(self):
        self.queue = collections.deque()

    def push(self, x: int) -> None:
        q = self.queue
        q.append(x)
        for _ in range(len(q)-1):
            q.append(q.popleft())
        self.queue = q

    def pop(self) -> int:
        return self.queue.popleft()

    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        return not self.queue
    
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()