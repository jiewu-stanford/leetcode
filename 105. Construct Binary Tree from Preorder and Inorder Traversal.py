'''
Title     : 105. Construct Binary Tree from Preorder and Inorder Traversal
Problem   : https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution
Reference: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if inorder:
            indx = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[indx])
            root.left = self.buildTree(preorder, inorder[:indx])
            root.right = self.buildTree(preorder, inorder[indx+1:])   # not necessary to truncate preorder, when we are done with left subtree the left half of preorder should already be empty
            return root
'''
iterative solution, it is very instructive to insert the following printout in the while loop and combine with the graph in the reference above to see each step
>>> print('the last preorder element in stack is {} whereas the inorder element reached is {}'.format(stack[-1], i))
Reference: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/214622/Precise-one-pass-iterative-solution-O(n)
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder: return None
        indx, root = 0, TreeNode(preorder[0])
        stack = [root]
        for i in preorder[1:]:
            parent = stack[-1]
            isLeft = True
            node = TreeNode(i)
            while stack and inorder[indx] == stack[-1].val:   # hit the leftmost node which is stack[-1] go back to parent and then check right
                parent = stack.pop()
                isLeft = False
                indx += 1
            if isLeft:
                parent.left = node
            else:
                parent.right = node
            stack.append(node)
        return root