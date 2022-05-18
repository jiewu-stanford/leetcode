'''
Title     : 255. Verify Preorder Sequence in Binary Search Tree ($$$)
Problem   : https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
          : https://www.lintcode.com/problem/verify-preorder-sequence-in-binary-search-tree/description
'''
'''
iterative solution walking through the array
Reference: http://pythonfiddle.com/leetcode-255verify-preorder-sequence-in-binary-search-tree/
'''
class Solution:
    def verifyPreorder(self, preorder):
        lowerbound = -float('inf')
        i = -1
        for val in preorder:
            if val < lowerbound:
                return False   # left subtree < root < right subtree
            if val > preorder[i]:
                while i >= 0 and val > preorder[i]:
                    lowerbound = preorder[i]
                    i -= 1
            i += 1
            preorder[i] = val
        return True
'''
DFS helper function divide-and-conquer narrowing [min, max] value range recursively
Reference: https://www.lintcode.com/problem/1307/solution/36890
'''
class Solution:
    def verifyPreorder(self, preorder):
        idx = 0
        def helper(mmin, mmax):
            nonlocal idx
            if idx == len(preorder):
                return True
            val = preorder[idx]
            if not mmin < val < mmax:
                return False
            idx += 1
            return helper(mmin, val) or helper(val, mmax)

        return helper(float('-inf'), float('inf'))