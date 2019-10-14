'''
Title     : 337. House Robber III
Problem   : https://leetcode.com/problems/house-robber-iii/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution, using a 2-tuple to keep track of max money for the two choices of (rob now, rob later) due to the alternating restriction
Reference: https://leetcode.com/problems/house-robber-iii/discuss/79394/Python-O(n)-code%3A-Optimized-for-Readability
'''
class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            if not node: return (0, 0)
            robleft = helper(node.left)
            robright = helper(node.right)
            robnow = node.val + robleft[1] + robright[1]   # rob node now then have to rob node.left and node.right later
            roblater = max(robleft) + max(robright)
            return (robnow, roblater)
        return max(helper(root))