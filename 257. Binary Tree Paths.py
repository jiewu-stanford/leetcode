'''
Title     : 257. Binary Tree Paths
Problem   : https://leetcode.com/problems/binary-tree-paths/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution without using helper function
Reference: https://leetcode.com/problems/binary-tree-paths/discuss/68287/5-lines-recursive-Python
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        return [str(root.val) + '->' + acc
                for child in (root.left, root.right) if child
                for acc in self.binaryTreePaths(child)] or [str(root.val)]
'''
recursive solution using helper function
Reference: https://leetcode.com/problems/binary-tree-paths/discuss/68272/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively)
'''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        self.helper(root, '', res)
        return res

    def helper(self, root, acc, res):
        if not root.left and not root.right:
            res.append(acc+str(root.val))
        if root.left:
            self.helper(root.left, acc+str(root.val)+'->', res)
        if root.right:
            self.helper(root.right, acc+str(root.val)+'->', res)

''' DFS + stack spelling out the recursive steps, ibid. '''
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res, stack = [], [(root, '')]
        while stack:
            node, s = stack.pop()
            if not node.left and not node.right:
                res.append(s + str(node.val))
            if node.right:
                stack.append((node.right, s+str(node.val)+'->'))
            if node.left:
                stack.append((node.left, s+str(node.val)+'->'))
        return res

''' BFS + queue, ibid. '''
from collections import deque
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root: return []
        res, queue = [], deque([(root, '')])
        while queue:
            node, s = queue.popleft()
            if not node.left and not node.right:
                res.append(s + str(node.val))
            if node.left:
                queue.append((node.left, s+str(node.val)+'->'))
            if node.right:
                queue.append((node.right, s+str(node.val)+'->'))
        return res