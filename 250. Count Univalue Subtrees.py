'''
Title     : 250. Count Univalue Subtrees ($$$)
Problem   : https://leetcode.com/problems/count-univalue-subtrees/
          : https://www.lintcode.com/problem/count-univalue-subtrees/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
DFS recursive helper function
Reference: https://leetcode.com/articles/count-univalue-subtrees/
'''
class Solution:
    def countUnivalSubtrees(self, root):
        if not root: return 0
        self.count = 0
        self.helper(root)
        return self.count
        
    def helper(self, node):
        if not node.left and not node.right:   # leaf is a univalue subtree
            self.count += 1
            return True
        univalue = True
        if node.left:
            univalue = self.helper(node.left) and univalue and node.left.val==node.val
        if node.right:
            univalue = self.helper(node.right) and univalue and node.right.val==node.val
        self.count += univalue
        return univalue

''' BFS recursive helper function, ibid. '''
class Solution:
    def countUnivalSubtrees(self, root):
        if not root: return 0
        self.count = 0
        self.helper(root, 0)
        return self.count

    def helper(self, node, val):   # value of parent node
        if not node: return True
        if not all([self.helper(node.left, node.val), self.helper(node.right, node.val)]):
            return False
        else:
            self.count += 1
        return node.val == val   # whether the univalue subtree node.left-node-node.right can be combined with the parent node to form a larger univalue subtree