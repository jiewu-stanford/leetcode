'''
Title     : 285. Inorder Successor in BST ($$$)
Problem   : https://leetcode.com/problems/inorder-successor-in-bst/description/
          : https://www.lintcode.com/problem/inorder-successor-in-bst/description
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive helper function exhausting all nodes in order, and then scan through the node list
Reference: https://blog.csdn.net/danspace1/article/details/86667504
'''
class Solution:
    def inorderSuccessor(self, root, p):
        def inOrder(root, nodes):
            if not root: return nodes
            nodes = inOrder(root.left, nodes)
            nodes.append(root)
            nodes = inOrder(root.right, nodes)
            return nodes

        nodes = inOrder(root, [])
        for i in range(len(nodes)):
            if nodes[i] == p:
                return nodes[i+1] if i+1 < len(nodes) else None

''' without searching through the entire tree but trace down through value comparison: if < then left vs. if > then right, ibid. '''
class Solution:
    def inorderSuccessor(self, root, p):
        res = None
        while root:
            if p.val < root.val:
                res = root
                root = root.left
            else:
                root = root.right
        return res