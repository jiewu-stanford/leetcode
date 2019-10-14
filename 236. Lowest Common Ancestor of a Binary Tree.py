'''
Title     : 236. Lowest Common Ancestor of a Binary Tree
Problem   : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
different from 235. now the LCA of a node can be itself, the consequence is that the recursive function can return None
Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/158060/Python-DFS-tm
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root: return None
        if p == root or q == root: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        # left, right = (self.lowestCommonAncestor(child, p, q) for child in (root.left, root.right))
        if left and right: return root
        return left or right    # equivalent to if not left: return right; if not right: return left
                                # can be further combined into: return root if left and right else left or right
'''
DFS stack iterative solution, find out all ancestors of p using while loop and then compare q with the ancestors of p
Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65236/JavaPython-iterative-solution
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = [root]
        parents = {root: None}
        while p not in parents or q not in parents:
            node = stack.pop()
            if node.left:
                parents[node.left] = node
                stack.append(node.left)
            if node.right:
                parents[node.right] = node
                stack.append(node.right)
                
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q
'''
DFS stack iterative solution, find out all paths leading to p and q and find their lowest intersection (AC by python but not python3)
Reference: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65245/Iterative-Solutions-in-PythonC%2B%2B
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findPath(root, target):
            path, stack = [], [root]
            while True:
                node = stack.pop()
                if node:
                    if node not in path[-1:]:
                        path += node,
                        if node == target: return path
                        stack += node, node.right, node.left
                    else:
                        path.pop()
                        
        pathp, pathq = findPath(root, p), findPath(root, q)
        res = root
        for i in range(0, min(len(pathp),len(pathq))):
            if pathp[i] == pathq[i]:
                res = pathp[i]
        return res