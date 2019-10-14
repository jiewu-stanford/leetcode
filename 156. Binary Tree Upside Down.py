'''
Title     : 156. Binary Tree Upside Down ($$$)
Problem   : https://leetcode.com/problems/binary-tree-upside-down/description/
          : https://www.lintcode.com/problem/binary-tree-upside-down/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
iterative solution
Reference: https://www.cnblogs.com/lightwindy/p/9689864.html
Graph: https://www.jianshu.com/p/6084b48f5b41
'''
class Solution:
    def upsideDownBinaryTree(self, root):
        node, parent, parentRight = root, None, None
        while node:
            nodeLeft = node.left
            node.left = parentRight
            parentRight = node.right
            node.right = parent
            parent = node
            node = nodeLeft
            # one-liner: parent, node.right, parentRight, node.left, node = node, parent, node.right, parentRight, node.left
        return parent

''' recursive solution, ibid. '''
class Solution:
    def upsideDownBinaryTree(self, root):
        return self.helper(root, None)
        
    def helper(self, node, parent):
        if not node: return parent
        root = self.helper(node.left, node)
        if parent:
            node.left = parent.right
        else:
            node.left = None
        node.right = parent
        return root