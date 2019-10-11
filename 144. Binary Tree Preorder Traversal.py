'''
Title     : 144. Binary Tree Preorder Traversal
Problem   : https://leetcode.com/problems/binary-tree-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
recursive solution
Reference: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45290/Python-solutions-(recursively-and-iteratively)
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:
            res.append(root.val)
            self.helper(root.left, res)
            self.helper(root.right, res)
'''
iterative solution, classical usage of stack's LIFO
Reference: https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45273/Very-simple-iterative-Python-solution
'''
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return res