'''
Title     : 343. Integer Break
Problem   : https://leetcode.com/problems/integer-break/
'''
'''
it reduces to decomposing into factors of 2 and 3, since any factor f > 4 can be replaced by 2*(f-2) to yield a larger product,
on the other hand more than two factors of 2 can be replaced by 3, since 3+3 = 2+2+2 but 3*3 > 2*2*2,
consolidating the above we conclude: the optimal decomposition will contain factors of 2 and/or 3 only, and the number of 2s will be no more than two
Reference: https://leetcode.com/problems/integer-break/discuss/80721/Why-factor-2-or-3-The-math-behind-this-problem
Reference: https://leetcode.com/problems/integer-break/discuss/80903/1-liner-in-Ruby-Python
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        return n - 1 if n < 4 else 3**((n-2)//3) * ((n-2)%3+2)
'''
explicit decomposition instead of one-liner (which also shows why n-2 is used in the one-liner)
Reference: https://leetcode.com/problems/integer-break/discuss/80757/Python-solution-(40ms)-with-explanation
'''
from functools import reduce
class Solution:
    def integerBreak(self, n: int) -> int:
        if n == 2: return 1
        if n == 3: return 2
        threeFactors = [3] * (n//3)
        threeMod = n % 3   # n % 3 = 0 --> (n-2)%3 + 2 = 3
        if threeMod == 1:
            threeFactors[0] += 1   # add to first '3' to get '4' = 2*2 --> (n-2)%3 + 2 = 4
        elif threeMod == 2:
            threeFactors.append(2)   # add an additional factor '2' --> (n-2)%3 + 2 = 2
        return reduce(lambda a,b: a*b, threeFactors)
'''
1D DP solution, without need to know the fact that the optimal decomposition will contain factors of 2 and/or 3 only and at most two factors of 2
let DP handle the optimal decomposition implicitly by trial-and-error: dp[i] = 1*max(dp[i-1],i-1) or 2*max(dp[i-2],i-2) or ... or j*max(dp[i-j],i-j) ... or (i-2)*max(dp[2], 2)
Reference: https://leetcode.com/problems/integer-break/discuss/80898/Python-DP-solution-with-explanation
'''
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i-1):
                dp[i] = max(dp[i], j*max(dp[i-j],i-j))
        return dp[-1]