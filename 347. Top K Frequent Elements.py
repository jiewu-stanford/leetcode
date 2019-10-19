'''
Title     : 347. Top K Frequent Elements
Problem   : https://leetcode.com/problems/top-k-frequent-elements/
'''
'''
use Counter() built-in .most_common() function, one-liner
Reference: https://leetcode.com/problems/top-k-frequent-elements/discuss/81639/1-line-Python-Solution-using-Counter-with-explanation
'''
import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mostFreq = collections.Counter(nums).most_common(k)
        return list(zip(*mostFreq))[0]
'''
use Counter() and then swap key and value to convert it to the 215. type problem, need max heap instead of min heap though
Reference: https://leetcode.com/problems/top-k-frequent-elements/discuss/177967/Python-or-Heap-%2B-Counter-tm
'''
import collections, heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = collections.Counter(nums)
        maxHeap = [(-freq, val) for val, freq in d.items()]
        heapq.heapify(maxHeap)
        for i in range(k):
            res.append(heapq.heappop(maxHeap)[1])
        return res
'''
use dict() to construct min heap and use heappop() to pop out the least frequent elements
Reference: https://leetcode.com/problems/top-k-frequent-elements/discuss/81643/Python-easy-to-understand-heap-solution
'''
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            d[num] = d.get(num,0) + 1
        heap = []
        for key in d.keys():
            heapq.heappush(heap, (d[key],key))
        
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res