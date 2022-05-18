'''
Title     : 23. Merge k Sorted Lists
Problem   : https://leetcode.com/problems/merge-k-sorted-lists/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
binary search like divide and conquer recursive solution: from merging K lists to merging 2 lists and then we can use the 21. solution!
Reference: https://leetcode.com/problems/merge-k-sorted-lists/discuss/10919/Python-concise-divide-and-conquer-solution
'''
class Solution(object):
    def mergeKLists(self, lists):
        if not lists: return
        if len(lists)==1: return lists[0]
        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2): return l1 or l2
        dummy = curr = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next
'''
use min heap to automate the sorting
Reference: https://leetcode.com/problems/merge-k-sorted-lists/discuss/183195/Python-heapq-solution
'''
import heapq
class Solution:
    def mergeKLists(self, lists):
        heap = []
        heapq.heapify(heap)
        count = 0   # to distinguish different nodes with the same value
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, count, lists[i]))
                count += 1

        head = curr = ListNode(0)
        while heap:
            count, node = heapq.heappop(heap)[1:]
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, count, node.next))
        return head.next
'''
use priority queue instead of min heap
Reference: https://leetcode.com/problems/merge-k-sorted-lists/discuss/10511/10-line-python-solution-with-priority-queue
tested in LintCode OJ: https://www.lintcode.com/problem/merge-k-sorted-lists/description
'''
import queue
class Solution:
    def mergeKLists(self, lists):
        pqueue = queue.PriorityQueue()
        count = 0
        for i in range(len(lists)):
            if lists[i]:
                pqueue.put((lists[i].val, count, lists[i]))
                count += 1

        head = curr = ListNode(0)
        while pqueue.qsize() > 0:
            count, node = pqueue.get()[1:]
            curr.next = node
            curr = curr.next
            if node.next:
                pqueue.put((node.next.val, count, node.next))
        return head.next