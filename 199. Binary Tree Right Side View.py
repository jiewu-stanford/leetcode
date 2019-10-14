'''
Title     : 199. Binary Tree Right Side View
Problem   : https://leetcode.com/problems/binary-tree-right-side-view/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution combining the right view of right subtree and the right view of left subtree (must extend beyond right subtree to be visible)
Reference: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56064/5-9-Lines-Python-48%2B-ms
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        right = self.rightSideView(root.right)
        left = self.rightSideView(root.left)
        return [root.val] + right + left[len(right):]

''' recursive solution, traversing right first then left, record the first node when a new depth is reach, ibid. '''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        def helper(node, depth):
            if node:
                if depth == len(res):   # check whether a new depth is reached
                    res.append(node.val)
                helper(node.right, depth+1)
                helper(node.left, depth+1)
        res = []
        helper(root, 0)
        return res

''' iterative solution, traverse each level and record the rightmost node (vs. the 107. solution), ibid. '''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res, nodes = [], [root]
        while nodes:
            res += nodes[-1].val,   # res.append([node.val for node in nodes])
            nodes = [child for node in nodes for child in (node.left, node.right) if child]
        return res
'''
iterative solution with stack, directly adapted from the 107. solution, note the LIFO order of stack
Reference: https://leetcode.com/problems/binary-tree-right-side-view/discuss/56248/Python-solutions-(DFS-recursively-DFS%2Bstack-BFS%2Bqueue)
'''
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        stack = [(root, 0)]
        res = []
        while stack:
            node, level = stack.pop()
            if node:
                if len(res) == level:
                    res.append(node.val)
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))   # right-side view thus right first
        return res