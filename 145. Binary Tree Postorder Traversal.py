'''
Title     : 145. Binary Tree Postorder Traversal
Problem   : https://leetcode.com/problems/binary-tree-postorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
recursive solution, compare with the 144. preorder traversal
Reference: https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45786/Python-recursive-and-iterative-solutions
'''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, root, res):
        if root:            
            self.helper(root.left, res)
            self.helper(root.right, res)
            res.append(root.val)

''' iterative solution, compare with the 144. preorder traversal, ibid. '''
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None: return []
        stack, res = [root], []
        while stack:
            node = stack.pop()
            if node:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res[::-1]