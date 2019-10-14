'''
Title     : 114. Flatten Binary Tree to Linked List
Problem   : https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution tracing down the tree
Reference: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36984/An-inorder-python-solution
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        if root.left:
            self.flatten(root.left)
            tail = root.left
            while tail.right:
                tail = tail.right   # go to the very end of the flattened left subtree to be connected to the to-be-flattened right subtree
            root.left, root.right, tail.right = None, root.left, root.right
        self.flatten(root.right)
'''
iterative solution using stack
Reference: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37310/A-solution-with-Python-generators-)
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        if not root: return
        prev = TreeNode(0)
        stack = [root]
        while stack:
            node = stack.pop()
            prev.right, prev.left = node, None
            prev = node
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)