'''
Title     : 103. Binary Tree Zigzag Level Order
Problem   : https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
step-by-step iterative solution directly adapted from the 107. solution
Reference: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33832/8-liner-Python
'''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, nodes, direction = [], [root], 1
        while nodes:
            res.append([node.val for node in nodes][::direction])
            direction *= -1
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return res
'''
BFS with deque solution directly adapted from the 107. solution
Reference: https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/34115/Python-short-iterative-solution-with-explanation
'''
import collections
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1: res.append([])   # without appending res[level] would produce index-out-of-bound error
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].insert(0, node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res

''' DFS with stack solution, ibid. '''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1: res.append([])
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].insert(0, node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res

''' recursive solution, ibid. '''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        self.helper(root, 0, res)
        return res
    
    def helper(self, node, level, res):
        if node:
            if len(res) < level+1: res.append([])
            if level % 2 == 0:
                res[level].append(node.val)
            else:
                res[level].insert(0, node.val)
            self.helper(node.left, level+1, res)   # queue.append((node.left, level+1))
            self.helper(node.right, level+1, res)