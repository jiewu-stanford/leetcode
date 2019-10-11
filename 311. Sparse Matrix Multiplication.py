'''
Title     : 311. Sparse Matrix Multiplication ($$$)
Problem   : https://leetcode.com/problems/sparse-matrix-multiplication/
          : https://www.lintcode.com/problem/sparse-matrix-multiplication/description
'''
'''
only sum A[i][k] * B[k][j] over i, j for non-zero A[i][k] and B[k][j]
Reference: https://www.cnblogs.com/lightwindy/p/9692836.html
'''
class Solution:
    def multiply(self, A, B):
        if not A or not B: return [[]]
        m, n, l = len(A), len(A[0]), len(B[0])
        res = [[0]*l for _ in range(m)]
        for i in range(m):
            for k in range(n):
                if A[i][k]:
                    for j in range(l):
                        if B[k][j]:
                            res[i][j] += A[i][k] * B[k][j]
        return res