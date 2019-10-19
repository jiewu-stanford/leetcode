'''
Title     : 305. Number of Islands II ($$$)
Problem   : https://leetcode.com/problems/number-of-islands-ii/description/
          : https://www.lintcode.com/problem/number-of-islands-ii/
'''
# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
'''
adapter the 323. solution to become a union find helper function
Reference: https://baihuqian.github.io/2018-08-02-number-of-islands-ii/
'''
class UnionFind:
    def __init__(self, r, c):
        self.components = {}
        for i in range(r):
            for j in range(c):
                id = self.coord2id(i, j, c)
                self.components[id] = id
                
    def coord2id(self, i, j, c):
        return i*c + j

    def unite(self, i, j):
        icomponent = self.findcomp(i)
        jcomponent = self.findcomp(j)
        if icomponent == jcomponent:
            return False
        else:
            self.components[min(icomponent, jcomponent)] = max(icomponent, jcomponent)
            return True

    def findcomp(self, i):
        if self.components[i] != i:
            self.components[i] = self.findcomp(self.components[i])
        return self.components[i]

class Solution:
    def numIslands2(self, n, m, operators):
        if not operators: return []
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        islands = [[0]*m for _ in range(n)]
        res = []
        uf = UnionFind(n, m)
        count = 0
        for i in range(len(operators)):
            count += 1
            ox = operators[i].x
            oy = operators[i].y
            if islands[ox][oy] != 1:
                islands[ox][oy] = 1
                oid = uf.coord2id(ox, oy, m)
                for dir in directions:
                    nx, ny = ox + dir[0], oy + dir[1]
                    if 0 <= nx < n and 0 <= ny < m and islands[nx][ny]==1:
                        nid = uf.coord2id(nx, ny, m)
                        ocomponent = uf.findcomp(oid)
                        ncomponent = uf.findcomp(nid)
                        if ocomponent != ncomponent:
                            uf.unite(oid, nid)
                            count -= 1
            res.append(count)
        return res