'''
Title     : 113. Path Sum II
Problem   : https://leetcode.com/problems/path-sum-ii/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

''' directly modify from 112. solution '''
''' recursive solution '''
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root: return []
        if not root.left and not root.right and root.val == sum:
            return [[root.val]]
        paths = self.pathSum(root.left, sum-root.val) + self.pathSum(root.right, sum-root.val)
        return [[root.val] + path for path in paths]

''' DFS stack solution '''
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> bool:
        if not root: return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            node, path = stack.pop()
            if node:
                if not node.left and not node.right and sum(path) == target:
                    res.append(path)
                if node.right:
                    stack.append((node.right, path+[node.right.val]))
                if node.left:
                    stack.append((node.left, path+[node.left.val]))
        return res

''' BFS queue solution '''
from collections import deque
class Solution:
    def pathSum(self, root: TreeNode, target: int) -> bool:
        if not root: return []
        res = []
        queue = deque([(root, [root.val])])
        while queue:
            node, path = queue.popleft()
            if node:
                if not node.left and not node.right and sum(path) == target:
                    res.append(path)
                if node.left:
                    queue.append((node.left, path+[node.left.val]))
                if node.right:
                    queue.append((node.right, path+[node.right.val]))
        return res