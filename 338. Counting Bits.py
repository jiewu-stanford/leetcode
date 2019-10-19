'''
Title     : 338. Counting Bits
Problem   : https://leetcode.com/problems/counting-bits/
'''
'''
insert the following into the for loop to see the process:
print('i = {}: binary i is {}, shift right by one bit gives {}, last bit AND gives {}'.format(i, bin(i), i>>1, i&1))
shift right by one bit allows lookup of previous result, add last bit AND to add back the possible '1' in the last bit which disappeared during right shift
Reference: https://leetcode.com/problems/counting-bits/discuss/79686/5-lines-of-Python-O(N)-time-simple-no-bitwise-operation
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        res = [0]*(num+1)
        for i in range(num+1):
            res[i] = res[i>>1] + (i & 1)
        return res