'''
Title     : 56. Merge Intervals
Problem   : https://leetcode.com/problems/merge-intervals/
'''
''' the key idea is that intervals can be sorted! '''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        res = [intervals[0]] if intervals else []
        for interval in intervals:
            if res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][-1], interval[1])
            else:
                res.append(interval)
        return res