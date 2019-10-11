'''
Title     : 296. Best Meeting Point ($$$)
Problem   : https://leetcode.com/problems/best-meeting-point/description/
          : https://www.lintcode.com/problem/best-meeting-point/description
'''
'''
the defining feature of Manhattan distance the distance is the sum of the row and column distance, which implies that we can minimize row and column distance independently
Reference: https://github.com/KrisYu/LeetCode-CLRS-Python/blob/master/296.%20Best%20Meeting%20Point.md
'''
class Solution:
    def minTotalDistance(self, grid):
        res = 0
        locations= []
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1: locations.append([i,j])

        locations.sort(key = lambda location: location[0])
        x = locations[len(locations)//2][0]   # mid point is the minimizing meeting point
        for location in locations:
            res += abs(location[0] - x)
        locations.sort(key = lambda location: location[1])
        y = locations[len(locations)//2][1]
        for location in locations:
            res += abs(location[1] - y)
        return res