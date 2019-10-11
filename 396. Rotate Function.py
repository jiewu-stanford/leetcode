'''
Title     : 396. Rotate Function
Problem   : https://leetcode.com/problems/rotate-function/
'''
'''
different rotations actually produce an arithmetic sequence with constant difference between adjacent rotations = sum(array) - last element * array length
Reference: https://leetcode.com/problems/rotate-function/discuss/195613/6-lines-Python-O(N)-time-O(1)-space-with-explanation
'''
class Solution:
    def maxRotateFunction(self, A: List[int]) -> int:
        k = len(A)
        res = curr = sum(i*j for i,j in enumerate(A))
        s = sum(A)
        while A:
            curr += s - A.pop() * k
            res = max(res, curr)
        return res