'''
Title     : 361. Bomb Enemy ($$$)
Problem   : https://leetcode.com/problems/bomb-enemy/description/
          : https://www.lintcode.com/problem/bomb-enemy/description
'''
'''
use helper function to count killed enemies for each cell of the grid, easy to understand but TLE
Reference: https://www.twblogs.net/a/5c9baf03bd9eee73ef4b0e0d
'''
class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        if not grid: return 0
        r, c = len(grid), len(grid[0])

        def count(x, y):
            if not grid: return 0
            leftkill, rightkill, upkill, downkill = 0, 0, 0, 0
            for i in range(x-1, -1, -1):
                if grid[i][y] == 'W': break
                if grid[i][y] == 'E': leftkill += 1
            for i in range(x+1, r):
                if grid[i][y] == 'W': break
                if grid[i][y] == 'E': rightkill += 1
            for j in range(y+1, c):
                if grid[x][j] == 'W': break
                if grid[x][j] == 'E': upkill += 1
            for j in range(y-1, -1, -1):
                if grid[x][j] == 'W': break
                if grid[x][j] == 'E': downkill += 1
            return leftkill + rightkill + upkill + downkill

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    res = max(res, count(i,j))
        return res
'''
simplify the counting by using adjacent walls to eliminate leftkill (thus rightkill = rowkill) and upkill (thus downkill == colkill)
Reference: https://www.jianshu.com/p/f5f55e4b4ce8
'''
class Solution:
    def maxKilledEnemies(self, grid):
        if not grid: return 0
        r, c = len(grid), len(grid[0])
        res, rowkill, colkill = 0, 0, [0]*c
        
        for i in range(r):
            for j in range(c):
                if j == 0 or grid[i][j-1] == 'W':               #   |--->
                    rowkill = 0
                    for k in range(j, c):
                        if grid[i][k] == 'W': break
                        if grid[i][k] == 'E': rowkill += 1
                if i == 0 or grid[i-1][j] == 'W':               #  ___
                    colkill[j] = 0                              #   |
                    for k in range(i, r):                       #   |
                        if grid[k][j] == 'W': break             #   V
                        if grid[k][j] == 'E': colkill[j] += 1
                if grid[i][j] == '0' and rowkill + colkill[j] > res:
                    res = rowkill + colkill[j]
        return res