'''
Title     : 138. Copy List with Random Pointer
Problem   : https://leetcode.com/problems/copy-list-with-random-pointer/
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random

''' Reference: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43485/Clear-and-short-python-O(2n)-and-O(n)-solution '''
import collections
class Solution(object):
    def copyRandomList(self, head):
        if not head: return
        d = collections.defaultdict(lambda: Node(0, None, None))
        d[None] = None   # otherwise the default value is Node(0, None, None)
        curr = head
        while curr:
            d[curr].val = curr.val
            d[curr].next = d[curr.next]
            d[curr].random = d[curr.random]   # d[None] = None
            curr = curr.next
        return d[head]
'''
iterative solution traversing and copying simultaneously without using dictionary
Reference: https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43689/Python-solution-without-using-dictionary
'''
class Solution(object):
    def copyRandomList(self, head):
        if not head: return

        curr = head
        while curr:   # insert an identical node after each node
            node = curr.next
            curr.next = Node(curr.val, None, None)
            curr.next.next = node
            curr = node

        curr = head
        while curr:   # copy random pointers
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        copyhead = curr = head.next
        while curr.next:   # separate the two: head list vs. curr list
            head.next = curr.next
            head = head.next
            curr.next = head.next
            curr = curr.next
        head.next = None
        return copyhead