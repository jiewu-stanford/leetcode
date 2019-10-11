'''
Title     : 67. Add Binary
Problem   : https://leetcode.com/problems/add-binary/
'''
''' Reference: https://leetcode.com/problems/add-binary/discuss/24562/One-line-Python-solution '''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(eval('0b' + a) + eval('0b' + b))[2:]
'''
recursive solution without using eval()
Reference: https://leetcode.com/problems/add-binary/discuss/24500/An-accepted-concise-Python-recursive-solution-10-lines
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if not a: return b
        if not b: return a
        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + str(int(a[-1]) + int(b[-1]))
'''
iterative solution using divmod()
Reference: https://leetcode.com/problems/add-binary/discuss/24683/10-line-Python-solution-easy-to-understand
'''
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = [ord(c)-48 for c in a[::-1]], [ord(c)-48 for c in b[::-1]]
        carry, res, la, lb = 0, [0]*max(len(a),len(b)), len(a), len(b)
        for i in range(len(res)):
            s = carry
            if i < la: s += a[i]
            if i < lb: s += b[i]
            carry, rem = divmod(s, 2)
            res[i] = chr(rem + 48)
        if carry: res.append('1')
        return ''.join(res[::-1])