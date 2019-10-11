'''
Title     : 362. Design Hit Counter ($$$)
Problem   : https://leetcode.com/problems/design-hit-counter/
'''
''' Reference: https://blog.csdn.net/danspace1/article/details/87810856 '''
class listNode():
    def __init__(self, timestamp):
        self.timestamp = timestamp
        self.next = None

class HitCounter:
    def __init__(self):
        self.data = []

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.data and timestamp - self.data[0] >= 300:
            self.data.pop(0)
        return len(self.data)

''' use queue(), ibid. '''
class HitCounter:
    def __init__(self):
        import collections
        self.data = collections.deque()

    def hit(self, timestamp: int) -> None:
        self.data.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.data and timestamp - self.data[0] >= 300:
            self.data.popleft()
        return len(self.data)

''' use defaultdict(), ibid. '''
class HitCounter:
    def __init__(self):
        import collections
        self.data = collections.defaultdict(int)

    def hit(self, timestamp: int) -> None:
        self.data[timestamp] = self.data.get(timestamp, 0) + 1

    def getHits(self, timestamp: int) -> int:
        res = [self.data[timestamp-i] for i in range(300)]
        return sum(res)

# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)