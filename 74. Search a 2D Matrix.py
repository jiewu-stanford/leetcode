'''
Title     : 74. Search a 2D Matrix
Problem   : https://leetcode.com/problems/search-a-2d-matrix/
'''
'''
multidimensional binary search
Reference: https://leetcode.com/problems/search-a-2d-matrix/discuss/26201/A-Python-binary-search-solution-O(logn)
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        r, c = len(matrix), len(matrix[0])
        l, r = 0, r*c-1
        while l <= r:
            mid = (l + r) // 2
            num = matrix[mid//c][mid%c]   # quick way to traverse matrix and locate the element
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
'''
flatten 2D matrix into 1D list and then binary search
Reference: https://leetcode.com/problems/search-a-2d-matrix/discuss/26399/Python-iterative-and-recursive-solutions
'''
from functools import reduce
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix: return False
        lst = sum(matrix, [])   # lst = reduce(lambda x,y: x+y, [row for row in matrix], [])
        l, r = 0, len(lst)-1
        while l <= r:
            mid = (l + r) // 2
            num = lst[mid]
            if num == target:
                return True
            elif num < target:
                l = mid + 1
            else:
                r = mid - 1
        return False