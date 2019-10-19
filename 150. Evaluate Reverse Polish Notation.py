'''
Title     : 150. Evaluate Reverse Polish Notation
Problem   : https://leetcode.com/problems/evaluate-reverse-polish-notation/
'''
'''
step-by-step iterative solution using stack
Reference: https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47444/Python-solution-with-comments-(don't-use-eval()-function)
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in ['+', '-', '*', '/']:
                stack.append(int(t))
            else:
                r, l = stack.pop(), stack.pop()
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                else:
                    if l*r < 0 and l%r != 0:
                        stack.append(l//r + 1)
                    else:
                        stack.append(l//r)
        return stack.pop()
'''
recursive solution using eval() function the problem reduces to expression concatenation
Reference: https://leetcode.com/problems/evaluate-reverse-polish-notation/discuss/47537/6-7-lines-in-Python
'''
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        t = tokens.pop()
        if t in '+-*/':
            b, a = map(self.evalRPN, [tokens]*2)
            t = eval('a' + t + 'b')
        return int(t)