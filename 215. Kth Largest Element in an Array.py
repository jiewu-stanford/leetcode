'''
Title     : 215. Kth Largest Element in an Array
Problem   : https://leetcode.com/problems/kth-largest-element-in-an-array/
'''
'''
Reference: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort)
Reference: https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60535/Python-min-heap-and-quick-partition-solutions-(O(nlogn)-and-O(n)-time-complexities)
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]

''' bubble sort, O(n*k) '''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(k):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        return nums[len(nums)-k]

''' selection sort, O(n*k) '''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums), len(nums)-k, -1):
            tmp = 0
            for j in range(i):
                if nums[j] > nums[tmp]:
                    tmp = j
            nums[tmp], nums[i-1] = nums[i-1], nums[tmp]
        return nums[len(nums)-k]

''' use heap.nlargest(), O(k+(n-k)logk) '''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums)[k-1]

''' use min heap structure and heappop(), O(k+(n-k)logk) '''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
        for _ in range(len(nums)-k):
            heapq.heappop(heap)
        return heapq.heappop(heap)

''' use min heap structure and heapreplace()/heappushpop(), O(k+(n-k)logk) '''
import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        return heap[0]