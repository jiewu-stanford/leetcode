'''
Title     : 252. Meeting Rooms ($$$)
Problem   : https://leetcode.com/problems/meeting-rooms/
          : https://www.lintcode.com/problem/meeting-rooms/description
'''
''' the key is to realize that we can also sort intervals '''
"""
Definition of Interval.
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals):
        intervals.sort(key=lambda interval: (interval.start, interval.end))
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False
        return True