'''
Title     : 116. Populating Next Right Pointers in Each Node
Problem   : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
'''
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
'''
recursive solution
Reference: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/discuss/37715/Python-solutions-(Recursively-BFS%2Bqueue-DFS%2Bstack)
'''
class Solution(object):
    def connect(self, root):
        if not root: return
        if root and root.left and root.right:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left   # 5 -> 6 in the example
            self.connect(root.left)
            self.connect(root.right)
        return root

''' BFS solution with deque(), ibid. '''
import collections
class Solution(object):
    def connect(self, root):
        if not root: return
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                queue.append(node.left)
                queue.append(node.right)
        return root

''' DFS solution with stack, ibid. '''
class Solution(object):
    def connect(self, root):
        if not root: return
        stack = [root]
        while stack:
            node = stack.pop()
            if node.left and node.right:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                stack.append(node.right)
                stack.append(node.left)
        return root