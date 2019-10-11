'''
Title     : 130. Surrounded Regions
Problem   : https://leetcode.com/problems/surrounded-regions/
'''
'''
DFS helper function, as the 'O's that would remain are those on the boundary and those adjacent to the boundary 'O's, we only need to check the boundry
Reference: https://leetcode.com/problems/surrounded-regions/discuss/209628/Python-solution
'''
class Solution(object):
    def solve(self, board):
        def dfs(x, y):
            visited[x][y] = 1
            board[x][y] = 'N'
            directions = [(0,1),(0,-1),(-1,0),(1,0)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < r and 0 <= ny < c and board[nx][ny]=='O' and visited[nx][ny]==0:
                    dfs(nx, ny)
        
        if not board: return
        r, c = len(board), len(board[0])
        if r <= 2 or c <= 2: return
        
        visited = [[0]*c for _ in range(r)]
        for i in range(r):
            if board[i][0] == 'O' and visited[i][0] == 0:
                dfs(i, 0)
            if board[i][c-1] == 'O' and visited[i][c-1] == 0:
                dfs(i, c-1)
        for j in range(c):
            if board[0][j] == 'O' and visited[0][j] == 0:
                dfs(0, j)
            if board[r-1][j] == 'O' and visited[r-1][j] == 0:
                dfs(r-1, j)
                
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
'''
BFS iterative solution using deque()
Reference: https://leetcode.com/problems/surrounded-regions/discuss/41652/Python-short-BFS-solution.
'''
import collections
class Solution(object):
    def solve(self, board):
        if not board: return
        r, c = len(board), len(board[0])
        if r <= 2 or c <= 2: return

        queue = collections.deque()
        for i in range(r):
            queue.append((i, 0))
            queue.append((i, c-1))
        for j in range(c):
            queue.append((0, j))
            queue.append((r-1, j))

        while queue:
            x, y = queue.popleft()
            if 0 <= x < r and 0 <= y < c and board[x][y]=='O':
                board[x][y] = 'N'
                queue.extend([(x-1,y),(x+1,y),(x,y-1),(x,y+1)])
            
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'N':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'