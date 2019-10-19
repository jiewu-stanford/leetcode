'''
Title     : 382. Linked List Random Node
Problem   : https://leetcode.com/problems/linked-list-random-node/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

''' Reference: https://leetcode.com/problems/linked-list-random-node/discuss/85718/Python-reservoir-sampling-solution-(when-the-length-of-linked-list-changes-dynamically '''
import random
class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        res, curr, indx = self.head, self.head.next, 1
        while curr:
            if random.randint(0, indx) is 0:
                res = curr
            curr = curr.next
            indx += 1
        return res.val
'''
random generator with buffer
Reference: https://leetcode.com/problems/linked-list-random-node/discuss/85673/%22buffered%22-reservoir-sampling
'''
import random
class Solution:
    def __init__(self, head: ListNode):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head   # instead of self.head.next
        before = 0
        buffer = [None] * 100
        while curr:
            indx = 0
            while curr and indx < 100:
                buffer[indx] = curr
                curr = curr.next
                indx += 1
            r = random.randrange(indx + before)
            if r < indx:
                res = buffer[r]
            before += indx
        return res.val

''' more straightforward and faster '''
import random
class Solution:
    def __init__(self, head: ListNode):
        self.nums = []
        while head:
            self.nums.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nums)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()