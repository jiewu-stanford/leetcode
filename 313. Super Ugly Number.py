'''
Title     : 313. Super Ugly Number
Problem   : https://leetcode.com/problems/super-ugly-number/
'''
'''
it is simply the generalization from the 264. solution to include arbitrary set of primes for ugly number generation
Reference: https://leetcode.com/problems/super-ugly-number/discuss/76303/Python-beat-93.68
'''
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        ugly = [1]
        uIndx = [0]*len(primes)
        uglyNums = [1]*len(primes)
        umin = 1
        for i in range(n-1):
            for j in range(len(primes)):
                if uglyNums[j] == umin:
                    uglyNums[j] = ugly[uIndx[j]] * primes[j]    # u2, u3, u5 = 2*ugly[i2], 3*ugly[i3], 5*ugly[i5] in the 264. solution
                    uIndx[j] += 1                               # if umin == u2: i2 += 1; if umin == u3: i3 += 1; if umin == u5: i5 += 1 in 264. solution
            umin = min(uglyNums)
            ugly.append(umin)
        return ugly[-1]
'''
similar to the 264. solution each ugly number is generated from the previous one by multiplying one of the primes
since we select the minimum one from such multiplication a natural choice of data structure is min heap
Reference: https://leetcode.com/problems/super-ugly-number/discuss/234588/Easy-python-solution-use-heap
'''
import heapq
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglySet, heap = set([1]), [1]
        while n:
            umin = heapq.heappop(heap)
            for p in primes:
                ugly = umin * p
                if not ugly in uglySet:
                    heapq.heappush(heap, ugly)
                    uglySet.add(ugly)
            n -= 1
        return umin