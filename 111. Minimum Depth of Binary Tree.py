'''
Title     : 111. Minimum Depth of Binary Tree
Problem   : https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
DFS recursive solution
Reference: https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36239/Python-BFS-and-DFS-solutions
'''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left and not root.right: return 1
        if root.left and not root.right:
            return 1 + self.minDepth(root.left)
        if root.right and not root.left:
            return 1 + self.minDepth(root.right)
        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))

''' DFS iterative solution using stack, ibid. '''
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res, stack = float('inf'), [(root, 1)]
        while stack:
            node, depth = stack.pop()
            if node:
                if not node.left and not node.right:
                    res = min(res, depth)
                if node.right:
                    stack.append((node.right, depth+1))
                if node.left:
                    stack.append((node.left, depth+1))
        return res

''' BFS iterative solution using deque, ibid. '''
from collections import deque
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root: return 0
        res, queue = float('inf'), deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res = min(res, depth)
                if node.left:
                    queue.append((node.left, depth+1))
                if node.right:
                    queue.append((node.right, depth+1))
        return res