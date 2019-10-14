'''
Title     : 226. Invert Binary Tree
Problem   : https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
straightforward recursive solution
Reference: https://leetcode.com/problems/invert-binary-tree/discuss/62714/3-4-lines-Python
'''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

''' straightforward iterative solution using stack, ibid. '''
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack.append(node.right)
                stack.append(node.left)
        return root
'''
iterative solution, BFS using queue instead of DFS using stack
Reference: https://leetcode.com/problems/invert-binary-tree/discuss/62705/Python-solutions-(recursively-dfs-bfs).
'''
from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                queue.append(node.left)
                queue.append(node.right)
        return root