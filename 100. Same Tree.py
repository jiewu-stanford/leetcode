'''
Title     : 100. Same Tree
Problem   : https://leetcode.com/problems/same-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
straightforward recursive solution
Reference: https://leetcode.com/problems/same-tree/discuss/32729/Shortest%2Bsimplest-Python
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return p is q
'''
iterative DFS solution with stack
Reference: https://leetcode.com/problems/same-tree/discuss/32894/Python-Recursive-solution-and-DFS-Iterative-solution-with-stack-and-BFS-Iterative-solution-with-queue
'''
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        stack = [(p, q)]
        while stack:
            n1, n2 = stack.pop()
            if n1 and n2 and n1.val == n2.val:
                stack.append((n1.right, n2.right))
                stack.append((n1.left, n2.left))
            elif not n1 and not n2:
                continue
            else:
                return False
        return True