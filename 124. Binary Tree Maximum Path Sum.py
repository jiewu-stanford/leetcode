'''
Title     : 124. Binary Tree Maximum Path Sum
Problem   : https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
bottom-up + postorder + recursive helper function
note that we only need to compare the four cases (1) none of left/right tree (2) add left tree (3) add right tree (4) add both tree
>> lmax = self.maxPathSum(root.left)
>> rmax = self.maxPathSum(root.right)
>> max(root.val, root.val+lmax, root.val+rmax, root.val+lmax+rmax)
because we are allowed to include partial instead of complete left/right tree
Reference: https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39813/Python-Solution-with-Detailed-Explanation
'''
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = root.val
        self.helper(root)
        return self.res
    
    def helper(self, root):
        if not root: return 0
        lmax = self.helper(root.left)
        rmax = self.helper(root.right)
        self.res = max(self.res, lmax+rmax+root.val)
        cumsum = max(lmax, rmax) + root.val   # lmax + rmax + root.val >= max(lmax, rmax) + root.val always because lmax, rmax >= 0
        return cumsum if cumsum > 0 else 0