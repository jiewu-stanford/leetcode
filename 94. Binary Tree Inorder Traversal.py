'''
Title     : 94. Binary Tree Inorder Traversal
Problem   : https://leetcode.com/problems/binary-tree-inorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
recursive solution, compare with the 144. preorder traversal
Reference: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381/Python-recursive-and-iterative-solutions
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:            
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

''' iterative solution, compare with the 144. preorder traversal, ibid. '''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        stack, res = [], []   # stack, res = [root], [] for preorder
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
'''
an alternative implementation, assign root to a variable node
Reference: https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31350/Easy-to-understand-Python-code-beats-96.42-Python-submissions
'''
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        stack, res = [root], []
        node = root
        while stack:
            while node and node.left:
                stack.append(node.left)
                node = node.left
            node = stack.pop()
            res.append(node.val)
            node = node.right
            if node:
                stack.append(node)
        return res