'''
Title     : 270. Closest Binary Search Tree Value ($$$)
Problem   : https://leetcode.com/problems/closest-binary-search-tree-value/description/
          : https://www.lintcode.com/problem/closest-binary-search-tree-value/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
        
''' Reference: http://www.voidcn.com/article/p-phbluudb-qp.html '''
class Solution:
    def closestValue(self, root, target):
        nums = []
        while root:
            nums += root.val,   # , to convert int to tuple for iterables
            root = root.left if target < root.val else root.right   # using BST structure to avoid seaching for the entire tree
        return min(nums, key=lambda x: abs(target-x))

''' recursive solution, ibid. '''
class Solution:
    def closestValue(self, root, target):
        child = root.left if target < root.val else root.right
        if not child: return root.val
        value = self.closestValue(child, target)
        return min((value, root.val), key=lambda x: abs(target-x))