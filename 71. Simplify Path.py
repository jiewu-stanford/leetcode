'''
Title     : 71. Simplify Path
Problem   : https://leetcode.com/problems/simplify-path/
'''
''' Reference: https://leetcode.com/problems/simplify-path/discuss/25794/Python-easy-to-understand-solutions-with-stack-and-deque '''

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item not in ['.','..','']:
                stack.append(item)
            if item == '..' and stack:
                stack.pop()
        return '/' + '/'.join(stack)

import collections
class Solution:
    def simplifyPath(self, path: str) -> str:
        queue = collections.deque()
        for item in path.split('/'):
            if item not in ['.','..','']:
                queue.append(item)
            if item == '..' and queue:
                queue.pop()
        return '/' + '/'.join(queue)