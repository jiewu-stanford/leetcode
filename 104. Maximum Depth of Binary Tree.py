'''
Title     : 104. Maximum Depth of Binary Tree
Problem   : https://leetcode.com/problems/maximum-depth-of-binary-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
''' one-line recursive '''
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) if root else 0
        # return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
'''
BFS + deque(), based on the fact that in BFS for a tree the depth of the last tree node should be the maximal height of the tree (vs. the 111. solution)
Reference: https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34434/Python-solution-(BFS-%2B-dequequeue)
'''
from collections import deque
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root: return 0
        queue = deque([(root, 1)])
        while queue:
            node, depth = queue.popleft()
            if node.left:
                queue.append((node.left, depth+1))
            if node.right:
                queue.append((node.right, depth+1))
        return depth