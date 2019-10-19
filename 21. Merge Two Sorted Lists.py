'''
Title     : 21. Merge Two Sorted Lists
Problem   : https://leetcode.com/problems/merge-two-sorted-lists/description/
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
'''
iterative solution
Reference: https://leetcode.com/problems/merge-two-sorted-lists/discuss/9735/Python-solutions-(iteratively-recursively-iteratively-in-place)
'''
class Solution(object):
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
        curr.next = l1 or l2   # one of the two lists is exhausted
        return dummy.next
'''
iterative in-place, assign curr.next to l2.next so as to break the l2 node link and make it point to l1 node, ibid.
Reference: https://www.youtube.com/watch?v=6ui3pEgOT70
'''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2): return l1 or l2
        dummy = curr = ListNode(0)
        dummy.next = l1   # produces error of 'NoneType object has no attribute next' at curr = curr.next if omitted
        while l1 and l2:
            if l1.val < l2.val:
                l1 = l1.next
            else:
                nxt = curr.next
                curr.next = l2
                tmp = l2.next
                l2.next = nxt
                l2 = tmp
                # one-liner: l2.next, curr.next, l2 = curr.next, l2, l2.next
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next

''' recursive solution, ibid. '''
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if None in (l1, l2): return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2