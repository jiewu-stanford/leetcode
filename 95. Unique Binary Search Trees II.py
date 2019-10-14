'''
Title     : 95. Unique Binary Search Trees II
Problem   : https://leetcode.com/problems/unique-binary-search-trees-ii/description/
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
DFS recursive helper function
Reference: https://leetcode.com/problems/unique-binary-search-trees-ii/discuss/31592/Recursive-python-solution
'''
class Solution(object):
    def generateTrees(self, n):
        if n == 0: return None
        return self.helper(1, n+1)
    
    def helper(self, start, end):
        if start == end: return None
        res = []
        for mid in range(start, end):
            for ltree in self.helper(start, mid) or [None]:
                for rtree in self.helper(mid+1, end) or [None]:
                    node = TreeNode(mid)
                    node.left, node.right = ltree, rtree
                    res.append(node)
        return res