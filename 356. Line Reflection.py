'''
Title     : 356. Line Reflection ($$$)
Problem   : https://leetcode.com/problems/line-reflection/description/
          : https://www.lintcode.com/problem/line-reflection/description
'''
'''
if mirror symmetric then the bisecting line should pass through xmid = (xmin + xmax)/2, cancel mirror symmetric point pairs to see whether there is leftover
Reference: https://github.com/NEWBEE108/LeetCode/blob/master/Python/line-reflection.py
'''
import collections
class Solution:
    def isReflected(self, points):
        if not points: return True
        xvals = []
        ygroups = collections.defaultdict(set)
        for p in points:
            ygroups[p[1]].add(p[0])   # group points with the same y-coordinate
            xvals.append(p[0])
        xmid = (max(xvals) + min(xvals))/2
        for xgroup in ygroups.values():
            for x in xgroup:
                if 2*xmid - x not in xgroup:
                    return False
        return True

''' two-pointer strategy based on sorting to avoid grouping by y, ibid '''
import collections
class Solution:
    def isReflected(self, points):
        if not points: return True
        points.sort()
        xmid = (points[0][0] + points[-1][0])/2
        l, r = 0, len(points)-1
        while l <= r:
            if 2*xmid != points[l][0]+points[r][0] or (points[l][0]!=points[r][0] and points[l][1]!=points[r][1]):
                return False
            l += 1;  r -= 1
        return True