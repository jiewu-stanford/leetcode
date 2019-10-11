'''
Title     : 73. Set Matrix Zeroes
Problem   : https://leetcode.com/problems/set-matrix-zeroes/
'''
'''
two steps: (1) mask up the element to be set 0 (2) set the masked element to 0
Reference: https://leetcode.com/problems/set-matrix-zeroes/discuss/26026/O(1)-space-solution-in-Python
'''
class Solution(object):
    def setZeroes(self, matrix):
        r, c = len(matrix), len(matrix[0])
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    for k in range(r):
                        if matrix[k][j] != 0:   # do not mask entries that are 0
                            matrix[k][j] = 'a'
                    for k in range(c):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'a'
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 'a':
                    matrix[i][j] = 0