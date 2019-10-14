'''
Title     : 298. Binary Tree Longest Consecutive Sequence ($$$)
Problem   : https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/description/
          : https://www.lintcode.com/problem/binary-tree-longest-consecutive-sequence/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
recursive helper function
Reference: https://www.jasonjson.com/archivers/binary-tree-longest-consecutive-sequence.html
Reference: https://www.jianshu.com/p/ebabdeed9bca
'''
class Solution:
    def longestConsecutive(self, root):
        if not root: return 0
        self.res = 0
        self.helper(root, 1)
        return self.res

    def helper(self, root, currLen):
        if not root: return 0
        self.res = max(self.res, currLen)
        if root.left:
            if root.left.val == root.val + 1:
                self.helper(root.left, currLen+1)
            else:
                self.helper(root.left, 1)
        if root.right:
            if root.right.val == root.val + 1:
                self.helper(root.right, currLen+1)
            else:
                self.helper(root.right, 1)