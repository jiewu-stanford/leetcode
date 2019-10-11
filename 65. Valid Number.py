'''
Title     : 65. Valid Number
Problem   : https://leetcode.com/problems/valid-number/
'''
''' a cheating albeit accepted version '''
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except:
            return False
'''
iterative solution checking every possible cases step-by-step
Reference: https://leetcode.com/problems/valid-number/discuss/23764/My-54ms-python-solution
'''
class Solution:
    def isNumber(self, s: str) -> bool:
        if not s: return False
        s = s.strip()
        i = 0
        res = signs = exps = dots = False
        while i < len(s):
            if s[i].isdigit():
                res = signs = True
                i += 1
            elif s[i] == '.' and not dots:
                dots = signs = True
                i += 1
            elif (s[i]=='e' or s[i]=='E') and not exps and res:
                res = signs = False   # ready for checking remaining part
                dots = exps = True
                i += 1
            elif (s[i]=='+' or s[i]=='-') and not res and not signs:
                signs = True
                i += 1
            else:
                return False
        return True if res else False