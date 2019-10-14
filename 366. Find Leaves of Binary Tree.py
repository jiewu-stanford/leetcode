'''
Title     : 366. Find Leaves of Binary Tree ($$$)
Problem   : https://leetcode.com/problems/find-leaves-of-binary-tree/description/
          : https://www.lintcode.com/problem/find-leaves-of-binary-tree/description
'''
# Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
'''
recursive helper function, leaves all have level 1 therefore level is different from depth!
Reference: https://blog.csdn.net/danspace1/article/details/87738403
'''
import collections
class Solution:
    def findLeaves(self, root):
        if not root: return []
        def getLevel(root, d):
            if not root: return 0
            left = getLevel(root.left, d)
            right = getLevel(root.right, d)
            level = 1 + max(left, right)
            d[level].append(root.val)
            return level

        d = collections.defaultdict(list)
        getLevel(root, d)
        res = []
        for k in sorted(d.keys()):
            res.append(d[k])
        return res