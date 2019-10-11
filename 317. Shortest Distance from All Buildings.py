'''
Title     : 317. Shortest Distance from All Buildings ($$$)
Problem   : https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
          : https://www.lintcode.com/problem/shortest-distance-from-all-buildings/description
'''
'''
BFS solution calculating the total distance from a given grid cell to all buildings (trace back/search from each building)
Reference: https://github.com/ShiqinHuo/LeetCode-Python/blob/master/Python/shortest-distance-from-all-buildings.py
'''
class Solution:
    """
    @param grid: the 2D grid, each cell is either 0, 1, 2 representing empty, building, obstacle
    """
    def shortestDistance(self, grid):
        def helper(grid, dists, counts, x, y):
            dist, r, c = 0, len(grid), len(grid[0])
            visited = [[False]*c for _ in range(r)]
            visited[x][y] = True
            prev = [(x, y)]
            while prev:
                dist += 1
                curr = []
                for i, j in prev:
                    for dir in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        ni, nj = i+dir[0], j+dir[1]
                        if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 0 and not visited[ni][nj]:
                            counts[ni][nj] += 1
                            dists[ni][nj] += dist
                            visited[ni][nj] = True
                            curr.append((ni, nj))
                prev = curr

        r, c, count = len(grid), len(grid[0]), 0
        dists = [[0]*c for _ in range(r)]
        counts = [[0]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    count += 1
                    helper(grid, dists, counts, i, j)   # a building reached, trace back to all empty grid cells to find the distance to the building
        
        shortest = float('inf')
        for i in range(r):
            for j in range(c):
                if dists[i][j] < shortest and counts[i][j] == count:
                    shortest = dists[i][j]

        return shortest if shortest != float('inf') else -1