'''
Title     : 373. Find K Pairs with Smallest Sums
Problem   : https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
'''
'''
find all products and sort
Reference: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84550/Slow-1-liner-to-Fast-solutions
'''
import itertools
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        return sorted(itertools.product(nums1, nums2), key=sum)[:k]
'''
BFS with min heap to take care of the sorting automatically
Reference: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/84642/9-lines-in-Python
'''
import heapq
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for n1 in nums1:
            for n2 in nums2:
                if len(heap) < k:
                    heapq.heappush(heap, (-n1-n2, [n1,n2]))   # default is min heap thus we store negated sum
                else:
                    if -heap[0][0] > n1 + n2:
                        heapq.heapreplace(heap, (-n1-n2, [n1,n2]))
                    else:
                        break
        return [heapq.heappop(heap)[1] for _ in range(k) if heap]