'''
Title     : 295. Find Median from Data Stream
Problem   : https://leetcode.com/problems/find-median-from-data-stream/
'''
'''
using two heaps, one min heap storing larger half (default of python) and one max heap storing smaller half (use -num)
Reference: https://leetcode.com/problems/find-median-from-data-stream/discuss/74047/JavaPython-two-heap-solution-O(log-n)-add-O(1)-find
heappushpop()  vs. heapreplace() = replace the smallest value
Reference: https://stackoverflow.com/questions/33701160/python-heapq-difference-between-heappushpop-and-heapreplace
'''
from heapq import *
class MedianFinder:
    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        if len(self.small) == len(self.large):
            heappush(self.large, -heappushpop(self.small, -num))
        else:
            heappush(self.small, -heappushpop(self.large, num))

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
            return float(self.large[0] - self.small[0])/2.0
        else:
            return float(self.large[0])
'''
direct binary search without using heap structure, clear and straightforward albeit much slower
Reference: https://leetcode.com/problems/find-median-from-data-stream/discuss/343226/Python-simple-solutions
'''
class MedianFinder:
    def __init__(self):
        self.nums = []        

    def addNum(self, num: int) -> None:
        if not self.nums:
            self.nums.append(num)
            return
        l, r = 0, len(self.nums)-1
        while l < r:
            mid = (l + r) // 2
            if self.nums[mid] == num:
                self.nums.insert(mid, num)
                return
            elif self.nums[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        if self.nums[l] < num:
            self.nums.insert(l+1, num)
        else:
            self.nums.insert(l, num)

    def findMedian(self) -> float:
        mid = (0 + len(self.nums)-1) // 2
        if len(self.nums) % 2:
            return self.nums[mid]
        else:
            return (self.nums[mid] + self.nums[mid+1])/2.0