'''
Title     : 286. Walls and Gates ($$$)
Problem   : https://leetcode.com/problems/walls-and-gates/
          : https://www.lintcode.com/problem/walls-and-gates/description
'''
'''
DFS helper function
Reference: https://blog.csdn.net/danspace1/article/details/86615657
'''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return
        r, c = len(rooms), len(rooms[0])
        for i in range(r):
            for j in range(c):
                if rooms[i][j] == 0:
                    self.dfs(rooms, i, j, 0)

    def dfs(self, rooms, x, y, dist):
        if not 0 <= x < len(rooms) or not 0 <= y < len(rooms[0]) or rooms[x][y] < dist: return
        rooms[x][y] = dist
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        for dx, dy in directions:
            self.dfs(rooms, x+dx, y+dy, dist+1)
        
''' BFS iterative solution, ibid. '''
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return
        r, c = len(rooms), len(rooms[0])
        gates = [(i,j) for i in range(r) for j in range(c) if rooms[i][j]==0]
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        INF = 2**31 - 1
        for x, y in gates:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and rooms[nx][ny]==INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    gates.append((nx, ny))
'''
BFS iterative solution using deque()
Reference: https://www.cnblogs.com/lightwindy/p/8476860.html
'''
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms: return
        r, c = len(rooms), len(rooms[0])
        gates = deque([(i,j) for i in range(r) for j in range(c) if rooms[i][j]==0])
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        INF = 2**31 - 1
        while gates:
            x, y = gates.popleft()   # for x, y in gates:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and rooms[nx][ny]==INF:
                    rooms[nx][ny] = rooms[x][y] + 1
                    gates.append((nx, ny))