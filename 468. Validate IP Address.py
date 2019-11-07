'''
Title     : 468. Validate IP Address
Problem   : https://leetcode.com/problems/validate-ip-address/
'''
''' Reference: https://leetcode.com/problems/validate-ip-address/discuss/127153/Python-36-ms-try-and-except-simple-solution '''
class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip4, ip6 = IP.split("."), IP.split(":")
        if len(ip4) == 4:
            for num in ip4:
                try: 
                    if not (num[0] in '0123456789' and int(num) < 256 and (num[0] != "0" or num == "0")): return "Neither"
                except:
                    return "Neither"
            return "IPv4"
        elif len(ip6) == 8:
            for num in ip6:
                try: 
                    if not (num[0] in '0123456789abcdefABCDEF' and 0 <= int(num, 16) and len(num) <= 4): return "Neither"
                except:
                    return "Neither"
            return "IPv6"
        return "Neither"