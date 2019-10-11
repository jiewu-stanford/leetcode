'''
Title     : 251. Flatten 2D Vector ($$$)
Problem   : https://leetcode.com/problems/flatten-2d-vector/
          : https://www.lintcode.com/problem/flatten-2d-vector/description
'''
''' Reference: https://www.cnblogs.com/lightwindy/p/8577871.html '''

class Vector2D(object):

    def __init__(self, vec2d):
        self.row, self.col, self.vec2d = 0, 0, vec2d

    def next(self):
        self.col += 1
        return self.vec2d[self.row][self.col-1]

    def hasNext(self):
        while self.row < len(self.vec2d) and self.col == len(self.vec2d[self.row]):
            self.row, self.col = self.row + 1, 0
        return self.row < len(self.vec2d)

# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())