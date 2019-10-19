'''
Title     : 394. Decode String
Problem   : https://leetcode.com/problems/decode-string/
'''
''' Reference: https://leetcode.com/problems/decode-string/discuss/87662/Python-solution-using-stack '''
class Solution(object):
    def decodeString(self, s):
        stack, currNum, res = [], 0, ''
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(currNum)
                res = ''
                currNum = 0
            elif c == ']':
                num = stack.pop()
                prevStr = stack.pop()
                res = prevStr + num*res
            elif c.isdigit():
                currNum = currNum*10 + int(c)
            else:
                res += c
        return res
'''
recursive helper function
Reference: https://leetcode.com/problems/decode-string/discuss/87576/NO-STACK-O(n)-recursive-solution-in-Python
'''
class Solution(object):
    def decodeString(self, s):
        return self.helper(list(s)[::-1])

    def helper(self, s):
        res = ''
        while s:
            num = ''
            while s[-1] in '0123456789':
                num += s.pop()
            if num:
                num = int(num)
                s.pop()   # get rid of '[' to prepare for the alphabet read-in c = s.pop()
                res += self.helper(s) * num
            else:
                c = s.pop()
                if c not in '[]': res += c
                if c == ']': break
        return res