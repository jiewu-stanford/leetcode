'''
Title     : 333. Largest BST Subtree ($$$)
Problem   : https://leetcode.com/problems/largest-bst-subtree/description/
          : https://www.lintcode.com/problem/verify-preorder-sequence-in-binary-search-tree/description
'''
'''
iterative solution adapting the 98. solution to check whether it is a valid BST
Reference: https://github.com/kamyu104/LeetCode-Solutions/blob/master/Python/largest-bst-subtree.py
'''
class Solution(object):
    def largestBSTSubtree(self, root):
        if not root: return 0
        res = 1

        def helper(root):
            if not root:
                return 0, None, None
            if not root.left and not root.right:
                return 1, root.val, root.val
            leftSize, leftMin, leftMax = 0, root.val, root.val
            if root.left:
                leftSize, leftMin, leftMax = helper(root.left)
            rightSize, rightMin, rightMax = 0, root.val, root.val
            if root.right:
                rightSize, rightMin, rightMax = helper(root.right)
            size = 0
            if (not root.left or leftSize > 0) and (not root.right or rightSize > 0) and leftMax <= root.val <= rightMin:
                size = 1 + leftSize + rightSize
                res = max(res, size)
            return size, leftMin, rightMax

        helper(root)
        return res