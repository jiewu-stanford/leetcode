'''
Title     : 48. Rotate Image
Problem   : https://leetcode.com/problems/rotate-image/
'''
'''
first reverse the orders of rows by *matrix[::-1], then convert columns to rows by zip()
Reference: https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)
'''
class Solution(object):
    def rotate(self, matrix):
        matrix[:] = zip(*matrix[::-1])
'''
rotation can be decomposed into two operations (x, y) -> (y, x) -> (y, n-1-x)
'''
class Solution(object):
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for row in matrix:
            l, r = 0, n-1
            while l < r:
                row[l], row[r] = row[r], row[l]
                l += 1
                r -= 1