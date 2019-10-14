'''
Title     : 106. Construct Binary Tree from Inorder and Postorder Traversal
Problem   : https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
recursive solution, directly adapted from the 105. solution
Reference: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/discuss/34814/A-Python-recursive-solution
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if inorder:
            indx = inorder.index(postorder.pop())
            root = TreeNode(inorder[indx])
            root.right = self.buildTree(inorder[indx+1:], postorder)   # root.right first and then root.left
            root.left = self.buildTree(inorder[:indx], postorder)
            return root
'''
iterative solution, directly adapted from the 105. solution, the changes are: (1) preorder[0] --> postorder[-1] (2) preorder[1:] --> postorder[:-1][::-1]
(3) isLeft --> isRight (4) inorder[indx] --> inorder[~indx] (5) if isLeft: parent.left = node --> if isRight: parent.right = node
'''
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder or not inorder: return None
        indx, root = 0, TreeNode(postorder[-1])
        stack = [root]
        for i in postorder[:-1][::-1]:
            parent = stack[-1]
            isRight = True
            node = TreeNode(i)
            while stack and inorder[~indx] == stack[-1].val:   # hit the rightmost node which is stack[-1] go back to parent and then check left
                parent = stack.pop()
                isRight = False
                indx += 1
            if isRight:
                parent.right = node
            else:
                parent.left = node
            stack.append(node)
        return root