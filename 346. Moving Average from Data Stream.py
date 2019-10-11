'''
Title     : 346. Moving Average from Data Stream ($$$)
Problem   : https://leetcode.com/problems/moving-average-from-data-stream/
          : https://www.lintcode.com/problem/moving-average-from-data-stream/description
'''
class MovingAverage:
    
    def __init__(self, size):
        self._size = size
        self._array = []
        self._sum = 0

    def next(self, val):
        self._sum += val
        self._array.append(val)
        if len(self._array) > self._size:
            self._sum -= self._array.pop(0)
        return self._sum/len(self._array)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)