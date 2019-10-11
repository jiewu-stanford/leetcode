'''
Title     : 200. Number of Islands
Problem   : https://leetcode.com/problems/number-of-islands/
'''
'''
DFS recursive helper function with visited record
Reference: https://leetcode.com/problems/number-of-islands/discuss/56622/Python-dfs-solutions
'''
class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        r, c, count = len(grid), len(grid[0]), 0
        visited = [[False]*c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    self.dfs(grid, i, j, visited)
        return count

    def dfs(self, grid, i, j, visited):
        if not (0 <= i < len(grid)) or not (0 <= j < len(grid[0])) \
            or grid[i][j] == '0' or visited[i][j]: return
        visited[i][j] = True
        self.dfs(grid, i+1, j, visited)
        self.dfs(grid, i-1, j, visited)
        self.dfs(grid, i, j+1, visited)
        self.dfs(grid, i, j-1, visited)
'''
BFS helper function using deque(), instead of maintaining a visited record modify directly on the grid
Reference: https://leetcode.com/problems/number-of-islands/discuss/121164/Python-BFS-and-DFS-solution
'''
import collections
class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        r, c, count = len(grid), len(grid[0]), 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    count += 1
                    self.bfs(grid, i, j)
        return count

    def bfs(self, grid, i, j):
        r, c = len(grid), len(grid[0])
        queue = collections.deque()
        queue.append((i, j))
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        while queue:
            x, y = queue.popleft()
            for d in directions:
                nx, ny = x + d[0], y + d[1]
                if (0 <= nx < r) and (0 <= ny < c) and grid[nx][ny] == '1':
                    queue.append((nx, ny))
                    grid[nx][ny] = '0'   # turn '1' to '0' = marked as visited
'''
DFS iterative solution
Reference: https://leetcode.com/problems/number-of-islands/discuss/159799/Python-solution
'''
class Solution(object):
    def numIslands(self, grid):
        if not grid: return 0
        r, c, count = len(grid), len(grid[0]), 0
        visited = set()
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and (i,j) not in visited:
                    count += 1
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        visited.add((x, y))
                        for dir in directions:
                            nx, ny = x + dir[0], y + dir[1]
                            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == '1' and (nx,ny) not in visited:
                                stack.append((nx, ny))
        return count