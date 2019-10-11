'''
Title     : 32. Longest Valid Parentheses
Problem   : https://leetcode.com/problems/longest-valid-parentheses/description/
'''
'''
1D DP solution using stack to keep track of the last (not ALL!) unpaired '('
Reference: https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        dp = [0] * (len(s)+1)   # dp[i] = length of valid parentheses substring(s) ending at i, e.g. dp = [0, 0, 0, 2, 0, 4, 0] for s = ")()())"
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    j = stack.pop()   # pair up and cancel '(' and ')'
                    dp[i+1] = dp[j] + (i - j + 1)
        return max(dp)
'''
iterative solution using stack to play the role of dp[i] and at the same time store last unpaired '('
Reference: https://leetcode.com/problems/longest-valid-parentheses/discuss/123926/Best-Python-Solution-(Beats-100)
'''
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s: return 0
        stack, longest = [0], 0   # stack = [0]-->[0]-->[0,0]-->[2]-->[2,0]-->[4] for s = ")()())"
        for c in s:
            if c == '(':
                stack.append(0)
            else:
                if len(stack) > 1:
                    l = stack.pop()   # pair up and cancel '(' and ')'
                    stack[-1] += l + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]
        return longest