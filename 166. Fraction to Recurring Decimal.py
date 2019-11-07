'''
Title     : 166. Fraction to Recurring Decimal
Problem   : https://leetcode.com/problems/fraction-to-recurring-decimal/
'''
'''
Reference: https://leetcode.com/problems/fraction-to-recurring-decimal/discuss/51186/Fast-and-concise-python-solution-using-dictionary.
'''
class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        sign = '-' if numerator * denominator < 0 else ''
        head, remainder = divmod(abs(numerator), abs(denominator))
        tail, repeated = '', {}   # use a dictionary to check whether the fractional part is repeated e.g. 3/7 = 0.(428571)
        while remainder != 0:
            if remainder in repeated:
                tail = tail[:repeated[remainder]] + '(' + tail[repeated[remainder]:] + ')'
                break
            repeated[remainder] = len(tail)
            digit, remainder = divmod(remainder*10, abs(denominator))
            tail += str(digit)
        return sign + str(head) + ('.'+tail if tail else tail)