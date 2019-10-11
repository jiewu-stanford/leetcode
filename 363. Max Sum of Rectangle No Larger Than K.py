'''
Title     : 363. Max Sum of Rectangle No Larger Than K
Problem   : https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/
'''
'''
brute force iterative solution, two pointers (l, r) define the column range of submatrix, summing over rows to find the submatrix sum
Reference: https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/discuss/83599/Accepted-C%2B%2B-codes-with-explanation-and-references
Reference: https://www.youtube.com/watch?time_continue=804&v=yCQN096CwWM
'''
import bisect
class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        res = -float('inf')
        for l in range(cols):
            colsum = [0] * rows
            for r in range(l, cols):
                cumsum, rowsum = [0], 0
                for i in range(rows):
                    colsum[i] += matrix[i][r]
                    rowsum += colsum[i]
                    indx = bisect.bisect_left(cumsum, rowsum-k)
                    if 0 <= indx < len(cumsum):
                        res = max(res, rowsum-cumsum[indx])   # since cumsum[indx] is the smallest element > rowsum-k, rowsum - cumsum[indx] is the largest element < k
                    bisect.insort(cumsum, rowsum)
        return res