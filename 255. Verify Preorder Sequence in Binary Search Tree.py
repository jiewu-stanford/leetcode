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