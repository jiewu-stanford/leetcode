'''
Title     : 227. Basic Calculator II
Problem   : https://leetcode.com/problems/basic-calculator-ii/description/
'''
''' Reference: https://leetcode.com/problems/basic-calculator-ii/discuss/63128/Python-140ms-solution-with-comments '''
class Solution(object):
    def calculate(self, s):
        s = s + "+"   # invoke the first elif() block to finish up the last addition/subtraction
        res, num, sign, stack = 0, 0, 1, []   # same as in the 224. solution
        for c in s:
            if c.isdigit():
                num = 10*num + int(c)   # *10 to promote the previous digit to higher power of 10
            elif c in ['-','+']:
                # block for evaluating multiplication/division which has precedence over addition/subtraction
                if stack and stack[-1] in ['*','/']:
                    mulordiv = stack.pop()
                    val = stack.pop()
                    num = val*num if mulordiv == '*' else val//num
                res += sign * num                
                sign = 1 if c == '+' else -1   # get sign ready for next number or brackets
                num = 0   # number added thus reset
            elif c in ['*','/']:   # very similar to the preceding elif(), just replace res += sign*num with stack.extend
                if stack and stack[-1] in ['*','/']:
                    mulordiv = stack.pop()
                    val = stack.pop()
                    num = val*num if mulordiv == '*' else val//num
                stack.extend([num, c])
                num = 0   # product/quotient stored thus reset
        return res