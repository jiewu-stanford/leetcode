'''
Title     : 253. Meeting Rooms II ($$$)
Problem   : https://leetcode.com/problems/meeting-rooms-ii/
          : https://www.lintcode.com/problem/meeting-rooms-ii/description
'''
'''
use a new heapq structure, whenever elements are pushed or popped or replaced the priority queue is preserved
Reference: https://blog.csdn.net/danspace1/article/details/86076499
'''
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        heap = []
        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heapreplace(heap, interval.end)
            else:
                heapq.heappush(heap, interval.end)
        return len(heap)
'''
without using heapq, instead use two sorted lists to record start time and end time
Reference: https://www.cnblogs.com/lightwindy/p/8577794.html
'''
class Solution:
    def minMeetingRooms(self, intervals):
        starts, ends = [], []
        for interval in intervals:
            starts.append(interval.start)
            ends.append(interval.end)
        starts.sort()
        ends.sort()
        s, e = 0, 0
        min_rooms, count = 0, 0
        while s < len(starts):
            if starts[s] < ends[e]:
                count += 1
                min_rooms = max(min_rooms, count)
                s += 1
            else:
                count -= 1   # to compensate for the next count += 1
                e += 1
        return min_rooms