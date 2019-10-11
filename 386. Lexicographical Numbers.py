'''
Title     : 386. Lexicographical Numbers
Problem   : https://leetcode.com/problems/lexicographical-numbers/description/
'''
'''
lexicographical ordering implies that we should really treat it as string rather than number, and it is much easier to sort string than number ('499999' vs. 499999)
Reference: https://leetcode.com/problems/lexicographical-numbers/discuss/86229/Python3-1-line-(sorting-229ms-beats-92.5-but-why)
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = map(str, range(1, n+1))
        return list(map(int, sorted(res)))
'''
iterative solution apending numbers one by one, e.g. 45 --> 450 (if) or 46 (elif) or 5 (else)
Reference: https://leetcode.com/problems/lexicographical-numbers/discuss/86228/The-most-elegant-python-solution-so-far.-10-liner.-iterative.-O(n)-time-O(1)-space.
'''
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res, curr = [], 1
        for i in range(1, n+1):
            res.append(curr)
            if curr * 10 <= n:
                curr *= 10
            elif curr % 10 != 9 and curr + 1 <= n:
                curr += 1
            else:
                while curr % 10 == 9 or curr == n: curr //= 10
                curr += 1
        return res