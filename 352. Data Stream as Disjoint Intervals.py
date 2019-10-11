'''
Title     : 352. Data Stream as Disjoint Intervals
Problem   : https://leetcode.com/problems/data-stream-as-disjoint-intervals/
'''
'''
use heapq structure to take care of the ascending order of intervals internally
Reference: https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82548/Share-my-python-solution-using-heap
'''
import heapq
class SummaryRanges:

    def __init__(self):
        self.intervals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heapq.heappush(self.intervals, [val,val])

    def getIntervals(self) -> List[List[int]]:
        res = []
        while self.intervals:
            curr = heapq.heappop(self.intervals)
            if res and curr[0] <= res[-1][1] + 1:
                res[-1][1] = max(res[-1][1], curr[1])
            else:
                res.append(curr)
        self.intervals = res
        return self.intervals
'''
use binary search
Reference: https://leetcode.com/problems/data-stream-as-disjoint-intervals/discuss/82546/simple-python-solution-with-binary-search
'''
class SummaryRanges(object):
    def __init__(self):
        self.intervals = []

    def addNum(self, val):
        low, high = 0, len(self.intervals)-1
        while low <= high:
            mid = (low + high) // 2
            interval = self.intervals[mid]
            if interval[0] <= val <= interval[1]:
                return
            elif val < interval[0]:
                high = mid - 1
            else:
                low = mid + 1
        pos = low
        self.intervals.insert(pos, [val, val])
        if pos+1 < len(self.intervals) and val == self.intervals[pos+1][0]-1:
            self.intervals[pos][1] = self.intervals[pos+1][1]
            self.intervals[pos+1:pos+2] = []
        if pos-1 >= 0 and val == self.intervals[pos-1][1]+1:
            self.intervals[pos-1][1] = self.intervals[pos][1]
            self.intervals[pos:pos+1] = []

    def getIntervals(self):
        return self.intervals

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()