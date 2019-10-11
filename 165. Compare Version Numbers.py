'''
Title     : 165. Compare Version Numbers
Problem   : https://leetcode.com/problems/compare-version-numbers/
'''
'''
iterative solution
Reference: https://leetcode.com/problems/compare-version-numbers/discuss/50952/Python-10-lines-solution
'''
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1s = [int(v) for v in version1.split('.')]
        v2s = [int(v) for v in version2.split('.')]
        for i in range(max(len(v1s), len(v2s))):
            v1 = v1s[i] if i < len(v1s) else 0
            v2 = v2s[i] if i < len(v2s) else 0
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
        return 0
'''
use zip_longest to go round the 1.0.0 problem
Reference: https://leetcode.com/problems/compare-version-numbers/discuss/51008/Concise-Python-code
'''
from itertools import zip_longest
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for i, j in zip_longest(version1.split('.'), version2.split('.'), fillvalue='0'):
            i, j = int(i), int(j)
            if i < j:
                return -1
            if i > j:
                return 1
        return 0