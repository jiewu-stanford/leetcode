'''
Title     : 102. Binary Tree Level Order Traversal
Problem   : https://leetcode.com/problems/binary-tree-level-order-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
many solutions: DFS recursive, DFS iterative + stack, BFS iterative + queue
Reference: https://leetcode.com/problems/binary-tree-level-order-traversal/discuss/33731/Python-short-dfs-solution
'''
''' DFS recursive '''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res
    
    def helper(self, root, level, res):
        if not root: return []
        if len(res) < level + 1:
            res.append([])
        res[level].append(root.val)
        self.helper(root.left, level+1, res)
        self.helper(root.right, level+1, res)

''' DFS iterative + stack '''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack, res = [(root, 0)], []
        while stack:
            curr, level = stack.pop()
            if curr:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(curr.val)
                if curr.right:
                    stack.append((curr.right, level+1))
                if curr.left:
                    stack.append((curr.left, level+1))
        return res

''' BFS iterative + deque() '''
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue, res = deque([(root, 0)]), []
        while queue:
            curr, level = queue.popleft()
            if curr:
                if len(res) < level + 1:
                    res.append([])
                res[level].append(curr.val)
                if curr.left:
                    queue.append((curr.left, level+1))
                if curr.right:
                    queue.append((curr.right, level+1))
        return res