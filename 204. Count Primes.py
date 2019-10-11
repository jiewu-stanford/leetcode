'''
Title     : 204. Count Primes
Problem   : https://leetcode.com/problems/count-primes/
'''
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2: return 0
        res = [True]*n
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                for j in range(2, (n-1)//i+1):   # the Sieve of Eratosthenes, can start from i instead of 2 to speed up
                    res[i*j] = False
        return sum(res)