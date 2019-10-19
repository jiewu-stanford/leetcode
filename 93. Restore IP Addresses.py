'''
Title     : 93. Restore IP Addresses
Problem   : https://leetcode.com/problems/restore-ip-addresses/
'''
'''
brute force list comprehension but very clear
Reference: https://leetcode.com/problems/restore-ip-addresses/discuss/30991/Python-3-lines-Brute-Force
'''
import itertools
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12: return []
        def isValid(s):
            return 0 <= int(s) < 256 and str(int(s)) == s   # no leading '0', no leading/trailing space
        return [s[:i] + '.' + s[i:j] + '.' + s[j:k] + '.' + s[k:]
                for i,j,k in itertools.combinations(range(1,len(s)),3)
                if isValid(s[:i]) and isValid(s[i:j]) and isValid(s[j:k]) and isValid(s[k:])]
'''
straightforward recursive function
Reference: https://leetcode.com/problems/restore-ip-addresses/discuss/31140/Python-easy-to-understand-solution-with-comments-(backtracking)
'''
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        self.helper(s, 0, '', res)
        return res

    def helper(self, s, startindex, acc, res):
        if startindex == 4:
            if not s: res.append(acc[:-1])   # [:-1] is to remove the last '.'
            return
        for i in range(1, 4):
            if i <= len(s):
                if i == 1:   # leading segment can be '0', ref. the test case "010010"
                    self.helper(s[i:], startindex+1, acc+s[:i]+'.', res)
                elif i == 2 and s[0] != '0':
                    self.helper(s[i:], startindex+1, acc+s[:i]+'.', res)
                elif i == 3 and s[0] != '0' and int(s[:3]) <= 255:
                    self.helper(s[i:], startindex+1, acc+s[:i]+'.', res)