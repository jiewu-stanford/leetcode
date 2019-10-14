'''
Title     : 107. Binary Tree Level Order Traversal II
Problem   : https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
step-by-step iterative solution without using stack or deque, use list.reverse() for reversal
Reference: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/35022/Short-python-solution
'''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        res, nodes = [], [root]
        while nodes:
            res.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        res.reverse()
        return res
'''
BFS with deque solution, use appendleft() to avoid reversal, also avoid appending to ensure res[level] does not produce index-out-of-bound error
Reference: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/35064/Python-solution-using-queue
'''
import collections
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([root])
        res = collections.deque()
        while queue:
            level = []
            for i in range(len(queue)):   # scan over and append the entire level, range not affected by the appending for next level below
                node = queue.popleft()
                level.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.appendleft(level)
        return list(res)
'''
BFS with deque solution, use reversal
Reference: Reference: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/discuss/34978/Python-solutions-(dfs-recursively-dfs%2Bstack-bfs%2Bqueue)
'''
import collections
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        queue = collections.deque([(root, 0)])
        res = []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1: res.append([])   # without appending res[level] would produce index-out-of-bound error
                res[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res[::-1]

''' DFS stack solution, ibid. '''
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root: return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) < level+1: res.append([])
                res[level].append(node.val)
                stack.append((node.right, level+1))
                stack.append((node.left, level+1))
        return res[::-1]