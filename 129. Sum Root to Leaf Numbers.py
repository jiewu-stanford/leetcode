'''
Title     : 129. Sum Root to Leaf Numbers
Problem   : https://leetcode.com/problems/sum-root-to-leaf-numbers/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
DFS recursive helper function
Reference: https://leetcode.com/problems/sum-root-to-leaf-numbers/discuss/41383/Python-solutions-(dfs%2Bstack-bfs%2Bqueue-dfs-recursively)
'''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        return self.helper(root, 0, 0)

    def helper(self, root, acc, res):
        if root:
            if not root.left and not root.right:
                res += acc*10 + root.val   # e.g. for 4-9 --> 4-9-1 in example 2, acc = 49, root.val = 1
            else:
                if root.left: res = self.helper(root.left, acc*10+root.val, res)
                if root.right: res = self.helper(root.right, acc*10+root.val, res)
        return res

''' DFS using stack to spell out the recursive step, ibid. '''
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                else:
                    if node.right:
                        stack.append((node.right, value*10+node.right.val))
                    if node.left:
                        stack.append((node.left, value*10+node.left.val))
        return res

''' BFS using queue, ibid. '''
from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0
        queue, res = deque([(root, root.val)]), 0
        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    res += value
                else:
                    if node.left:
                        queue.append((node.left, value*10+node.left.val))
                    if node.right:
                        queue.append((node.right, value*10+node.right.val))
        return res