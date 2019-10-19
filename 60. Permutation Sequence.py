'''
Title     : 60. Permutation Sequence
Problem   : https://leetcode.com/problems/permutation-sequence/description/
'''
'''
key fact: in a list of c! permutations, there will be c!/c permutations begining with a given digit, find out this leading digit using divmod() and apply the same argument to the remaining digits
for the example of n = 4 i.e. nums = [1,2,3,4] and k = 9 the iteration goes through (9, 3!, [1,2,3,4]) -> (3, 2!, [1,3,4]) -> (1, 1!, [1,4]) -> (0, 0!, [1])
Reference: https://leetcode.com/problems/permutation-sequence/discuss/22659/Python-concise-solution
Reference: https://leetcode.com/problems/permutation-sequence/discuss/353646/Faster-than-94.74-iterative-python-solution.-Thoroughly-explained!
'''
import math
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res, nums = '', list(range(1,n+1))
        k -= 1
        while n:
            n -= 1
            indx, k = divmod(k, math.factorial(n))   # trick: use divmod to delete the leading digit and work on the remaining permutations
            res += str(nums.pop(indx))
        return res