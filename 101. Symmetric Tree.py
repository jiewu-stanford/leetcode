'''
Title     : 101. Symmetric Tree
Problem   : https://leetcode.com/problems/symmetric-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
straightforward recursive solution, recycling the 100. solution
Reference: https://leetcode.com/problems/symmetric-tree/discuss/33325/Python-short-recursive-solution.
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        return self.isSameTree(root.left, root.right)

    def isSameTree(self, l, r):
        if l and r:
            return l.val == r.val and self.isSameTree(l.left, r.right) and self.isSameTree(l.right, r.left)
        else:
            return l is r
'''
iterative solution using the 100. solution i.e. consider root.left and root.right as two trees, then reflect root.left and compare
Reference: https://leetcode.com/problems/symmetric-tree/discuss/33050/Recursively-and-iteratively-solution-in-Python
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        stack = [(root.left, root.right)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.left, n2.right))
                stack.append((n1.right, n2.left))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True            
'''
iterative solution + symmetric list checking
Reference: https://leetcode.com/problems/symmetric-tree/discuss/33068/6line-AC-python
'''
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root: return True
        queue = [root]
        while queue:
            values = [node.val if node else None for node in queue]
            if values != values[::-1]:
                return False
            queue = [child for node in queue if node for child in (node.left, node.right)]
        return True