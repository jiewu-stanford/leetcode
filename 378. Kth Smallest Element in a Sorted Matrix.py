'''
Title     : 378. Kth Smallest Element in a Sorted Matrix
Problem   : https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''
''' most natural solution using list comprehension '''
class Solution(object):
    def kthSmallest(self, matrix, k):
        sorted([n for row in matrix for n in row])[k-1]
'''
use sum(matrix, []) to flatten 2D list to 1D list
Reference: https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85188/python-one-line-solution-...
'''
class Solution(object):
    def kthSmallest(self, matrix, k):
        return sorted(sum(matrix, []))[k-1]

''' same flattening can be done using itertools.chain, ibid. '''
import itertools
class Solution(object):
    def kthSmallest(self, matrix, k):
        return sorted(itertools.chain(*matrix))[k-1]

''' same flattening can be done using heaq.merge, ibid. '''
import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        return list(heapq.merge(*matrix))[k-1]