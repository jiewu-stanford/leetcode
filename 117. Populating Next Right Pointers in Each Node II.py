'''
Title     : 117. Populating Next Right Pointers in Each Node II
Problem   : https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
BFS O(N) solution using deque(), different from the 116. solution we need a variable to store nodes at the same level because the tree is no longer perfect binary
Reference: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/38013/Python-easy-to-understand-solution-(similar-to-level-order-traversal)
'''
import collections
class Solution(object):
    def connect(self, root):
        if not root: return
        queue = collections.deque([root])
        nextLevel = collections.deque([])
        while queue:
            node = queue.popleft()
            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
            if queue:
                node.next = queue[0]
            else:
                queue, nextLevel = nextLevel, queue
        return root
'''
iterative O(1) solution
Reference: https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/38035/Just-convert-common-BFS-solution-to-O(1)-space-a-simple-python-code
'''
class Solution(object):
    def connect(self, root):
        if not root: return
        node, nextLevel, curr = root, None, None
        while node:
            if node.left:
                if not nextLevel:
                    nextLevel = curr = node.left
                else:
                    curr.next = node.left
                    curr = curr.next
            if node.right:
                if not nextLevel:
                    nextLevel = curr = node.right
                else:
                    curr.next = node.right
                    curr = curr.next
            node = node.next
            if not node and nextLevel:
                node, nextLevel, curr = nextLevel, None, None
        return root