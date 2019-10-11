'''
Title     : 20. Valid Parentheses
Problem   : https://leetcode.com/problems/valid-parentheses/
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        d = {"]":"[", "}":"{", ")":"("}
        for c in s:
            if stack and c in d and stack[-1]==d[c]:
                stack.pop()
            else:
                stack.append(c)
        return not stack