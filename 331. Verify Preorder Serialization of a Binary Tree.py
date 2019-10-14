'''
Title     : 331. Verify Preorder Serialization of a Binary Tree
Problem   : https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/description/
'''
'''
simply count the number of available slots: null nodes occupy one thus -1, non-null nodes occupy one but create two new thus net +1
Reference: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78564/The-simplest-python-solution-with-explanation-(no-stack-no-recursion)
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        slots = 1   # +1 from root
        for node in nodes:
            if slots == 0: return False
            if node == '#':
                slots -= 1
            else:
                slots += 1
        return slots == 0
'''
iterative solution using stack
Reference: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/276605/Python-straightforward-stack
'''
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        nodes = preorder.split(',')
        stack = []
        for node in nodes:
            stack.append(node)
            while stack[-2:] == ['#','#']:   # leaf found
                stack.pop()
                stack.pop()
                if not stack:
                    return False
                else:
                    stack.pop()
                stack.append('#')   # delete the leaf
        return stack == ['#']
'''
recursive solution to check whether a node can be constructed
Reference: https://leetcode.com/problems/verify-preorder-serialization-of-a-binary-tree/discuss/78657/Short'n'Sweet-Recursive-Python-solution-beats-97
'''
import collections
class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        def helper(nodes):
            if not nodes: return True
            node = nodes.popleft()
            left, right = True, True
            if node != '#':
                left = helper(nodes)
                if not nodes:
                    return False
                right = helper(nodes)
            return left and right
    
        nodes = collections.deque(preorder.split(','))
        return helper(nodes) and not nodes   # no unconstructed nodes left