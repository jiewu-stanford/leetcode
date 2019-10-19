'''
Title     : 89. Gray Code
Problem   : https://leetcode.com/problems/gray-code/
'''
'''
iterative solution following the step-by-step construction: scan backward and append '1' in front
e.g. n = 3: 000, 001, 011, 010, 110, 111, 101, 100 = (00, 01, 11, 10) + add '1' in front of (10, 11, 01, 00)
Reference: https://leetcode.com/problems/gray-code/discuss/30007/Python-Easy-Bit-Manipulation-Solution
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if not n: return [0]
        res = [0, 1]
        for i in range(2, n+1):
            for j in range(len(res)-1, -1, -1):
                res.append(res[j] | 1 << i-1)
        return res
'''
recursive solution to produce (n-1)-code, then scan backward and append '1' in front, but instead of using bitwise OR add a power of 2 number N to append '1'
Reference: https://leetcode.com/problems/gray-code/discuss/30039/Python-recursive-solution-easy-understanding
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0: return [0]
        if n == 1: return [0, 1]
        res = self.grayCode(n - 1)
        N = pow(2, n-1)
        for i in range(N-1, -1, -1):
            res.append(res[i] + N)
        return res