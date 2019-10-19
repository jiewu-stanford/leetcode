'''
Title     : 224. Basic Calculator
Problem   : https://leetcode.com/problems/basic-calculator/description/
'''
''' Reference: https://leetcode.com/problems/basic-calculator/discuss/62424/Python-concise-solution-with-stack '''
class Solution(object):
    def calculate(self, s):
        res, num, sign, stack = 0, 0, 1, []
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)
            elif c in ['-','+']:
                res += sign * num
                num = 0
                sign = 1 if c == '+' else -1   # get sign ready for next number or brackets
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0     # '(' is the same as '+(', reset res for within bracket evaluation
            elif c == ')':
                res += sign * num
                num = 0
                res *= stack.pop()   # retrieve the sign
                res += stack.pop()   # add the evaluation result outside brackets
        return res + num * sign