'''
Title     : 110. Balanced Binary Tree
Problem   : https://leetcode.com/problems/balanced-binary-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution with depth memory using the 104. solution
Reference: https://leetcode.com/problems/balanced-binary-tree/discuss/35886/A-simple-Python-recursive-solution-172ms
'''
class Solution:
    def __init__(self):
        self.d = {}

    def isBalanced(self, root: TreeNode) -> bool:
        if not root: return True
        return abs(self.depth(root.left)-self.depth(root.right))<=1 and self.isBalanced(root.left) and self.isBalanced(root.right)
    
    def depth(self, root):
        if not root: return 0
        elif root in self.d: return self.d[root]
        else:
            self.d[root] = 1 + max(self.depth(root.left), self.depth(root.right))
            return self.d[root]
'''
DFS stack solution
Reference: https://leetcode.com/problems/balanced-binary-tree/discuss/128678/Python-3-iterative-and-recursive-solution
'''
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        stack = [(False, root)]
        depth = {None: 0}   # DFS thus search from bottom up, bottom depth = 0
        while stack:
            visited, node = stack.pop()
            if node is None: continue
            if not visited:
                stack.extend([(True, node), (False, node.right), (False, node.left)])
            else:
                if abs(depth[node.left] - depth[node.right]) > 1: return False
                depth[node] = max(depth[node.left], depth[node.right]) + 1
        return True