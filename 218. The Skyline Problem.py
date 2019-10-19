'''
Title     : 218. The Skyline Problem
Problem   : https://leetcode.com/problems/the-skyline-problem/description/
'''
'''
use min heap to sort negative height and examine at each vertical line (vlines) where there is a building starts or ends
Reference: https://leetcode.com/problems/the-skyline-problem/discuss/61210/14-line-python-code-straightforward-and-easy-to-understand
'''
import heapq
class Solution(object):
    def getSkyline(self, buildings):
        vlines = {l for b in buildings for l in (b[0],b[1])}
        res, i, heap = [], 0, []
        for vl in sorted(vlines):
            while i < len(buildings) and buildings[i][0] <= vl:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))   # record all buildings that starts before or at current vertical line
                i += 1
            while heap and heap[0][1] <= vl:
                heapq.heappop(heap)   # pop out the buildings that ends before or at current vertical line
            height = -heap[0][0] if heap else 0
            if not res or res[-1][1] != height:
                res.append((vl, height))
        return res