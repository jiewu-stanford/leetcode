'''
Title     : 109. Convert Sorted List to Binary Search Tree
Problem   : https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
'''
we can simply convert the given linked list to array (while head: ls.append(head.val); head = head.next) and then apply the 108. solution
Reference: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35526/Python-solutions-(convert-to-array-first-top-down-approach-bottom-up-approach)
but we can also work directly on the linked list, using the fast/slow pointer strategy to find the middle node as the root as in the 234. solution in lieu of binary search
Reference: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35474/Python-recursive-solution-with-detailed-comments-(operate-linked-list-directly)
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head: return
        if not head.next: return TreeNode(head.val)
        slow, fast, prev = head, head, None
        while fast and fast.next:
            prev, slow, fast = slow, slow.next, fast.next.next
        prev.next = None   # cut off the left half
        
        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
'''
DFS helper function, note that we should use inorder assignment (left -> root -> right) to automatically end up with the middle node as the root when building from bottom up
Reference: https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/discuss/35526/Python-solutions-(convert-to-array-first-top-down-approach-bottom-up-approach)
'''
class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        depth, node = 0, head
        while node:
            depth += 1
            node = node.next
        return self.helper([head], 0, depth-1)

    def helper(self, head, start, end):
        if start > end: return None
        mid = (start + end) // 2
        left = self.helper(head, start, mid-1)
        root = TreeNode(head[0].val)
        root.left = left
        head[0] = head[0].next
        root.right = self.helper(head, mid+1, end)
        return root