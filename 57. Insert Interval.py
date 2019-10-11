'''
Title     : 57. Insert Interval
Problem   : https://leetcode.com/problems/insert-interval/
'''
''' insert it and then apply the 56. solution '''
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]] if intervals else []
        for interval in intervals:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][-1], interval[1])
            else:
                res.append(interval)
        return res