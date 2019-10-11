'''
Title     : 327. Count of Range Sum
Problem   : https://leetcode.com/problems/count-of-range-sum/description/
'''
'''
O(n^2) solution to clarify the requirement on range sum (= current cumsum - previous cumsum):
lower <= (current cumsum - previous cumsum) <= upper is equivalent to: current cumsum - upper <= previous cumsum <= current cumsum - lower
Reference: https://leetcode.com/problems/count-of-range-sum/discuss/78016/Very-concise-solution-in-Python-with-explanation
'''
import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        res, curr, cumsums = 0, 0, [0]
        for num in nums:
            curr += num
            res += bisect.bisect_right(cumsums, curr-lower) - bisect.bisect_left(cumsums, curr-upper)   # how many cumsums fall within [curr-upper, curr-lower]
            bisect.insort(cumsums, curr)
        return res
'''
O(nlogn) solution using merge sort
Reference: https://leetcode.com/problems/count-of-range-sum/discuss/77991/Short-and-simple-O(n-log-n)
'''
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        cumsums = [0]
        for num in nums: cumsums.append(cumsums[-1]+num)
        def helper(l, r):
            mid = (l + r) // 2
            if mid == l: return 0
            count = helper(l, mid) + helper(mid, r)     # recursion taking care of range sums within each halves
            i = j = mid
            for prevsum in cumsums[l:mid]:              # for loop taking care of range sums across the two halves
                while i < r and cumsums[i] - prevsum < lower: i += 1
                while j < r and cumsums[j] - prevsum <= upper: j += 1
                count += j - i
            cumsums[l:r] = sorted(cumsums[l:r])   # merge sorted halves i.e. cumsums[l:r] = heapq.merge(cumsums[l:mid], cumsums[mid:r])
            return count
        return helper(0, len(cumsums))
'''
O(nlogn) solution using BIT
Reference: https://leetcode.com/problems/count-of-range-sum/discuss/77986/O(NlogN)-Python-solution-binary-indexed-tree-268-ms
'''
import bisect
class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        n = len(nums)
        cumsums, BITree = [0]*(n+1), [0]*(n+2)
        # BIT implementation
        def count(i):
            s = 0
            while i:
                s += BITree[i]
                i -= (i & -i)   # the position of the last bit '1' in binary form of i (https://stackoverflow.com/questions/15395317/meaning-of-bitwise-and-of-a-positive-and-negative-number)
            return s
        def update(i):
            while i <= n + 1:
                BITree[i] += 1
                i += (i & -i)

        for i in range(n):
            cumsums[i+1] = cumsums[i] + nums[i]
        res, sortsum = 0, sorted(cumsums)
        for cumsum in cumsums:
            cumcount = count(bisect.bisect_right(sortsum, cumsum-lower)) - count(bisect.bisect_left(sortsum, cumsum-upper))   # count() instead of just indx because it is sorted thus all 0,1,...,indx satisfy <= cumsum-lower
            res += cumcount
            update(bisect.bisect_left(sortsum, cumsum) + 1)
        return res