'''
Title     : 240. Search a 2D Matrix II
Problem   : https://leetcode.com/problems/search-a-2d-matrix-ii/
'''
'''
the ascending order in both row and col allows the normal search carried out simultaneously in both rows and columns
Reference: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/151818/Java-Python-Beats-100-with-Explanation
'''
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix: return False
        i, j = len(matrix)-1, 0
        while 0 <= i and j < len(matrix[0]):
            if matrix[i][j] < target:
                j += 1
            elif matrix[i][j] > target:
                i -= 1   # start from bottom left corner
            else:
                return True
        return False
'''
one-liner using any(), although O(m*n)
Reference: https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/66168/4-lines-C-6-lines-Ruby-7-lines-Python-1-liners
'''
class Solution:
    def searchMatrix(self, matrix, target):
        return any(target in row for row in matrix)