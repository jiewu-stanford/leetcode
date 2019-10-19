'''
Title     : 149. Max Points on a Line
Problem   : https://leetcode.com/problems/max-points-on-a-line/description/
'''
''' Reference: https://leetcode.com/problems/max-points-on-a-line/discuss/47108/Python-68-ms-code '''
import numpy as np
class Solution(object):
    def maxPoints(self, points):
        if not points: return 0
        l = len(points)
        res = 0
        for i in range(l):
            d = {'single-point': 1}
            duplicates = 0
            for j in range(i+1, l):
                x, y = points[j][0], points[j][1]
                if x == points[i][0] and y == points[i][1]:
                    duplicates += 1;    continue
                elif x == points[i][0] and y != points[i][1]:
                    slope = 'inf'
                else:
                    slope = ((points[i][1]-y)*np.longdouble(1))/(points[i][0]-x)   # np.longdouble is to cope with low float precision of python
                if slope not in d: d[slope] = 1
                d[slope] += 1
            res = max(res, max(d.values()) + duplicates)
        return res