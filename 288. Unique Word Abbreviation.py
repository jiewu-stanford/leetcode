'''
Title     : 288. Unique Word Abbreviation ($$$)
Problem   : https://leetcode.com/problems/unique-word-abbreviation/
          : https://www.lintcode.com/problem/unique-word-abbreviation/description
'''
''' Reference: https://czxttkl.wordpress.com/2015/10/09/leetcode-288-unique-word-abbreviation/ '''

class ValidWordAbbr:

    def __init__(self, dictionary):
        self.encoder = lambda s: s[0] + str(len(s)-2) + s[-1]
        abbrv = [(self.encoder(s), s) for s in dictionary]
        d = dict()
        for key, val in abbrv:
            if not d.get(key): d[key] = set()
            d[key].add(val)
        self.d = d

    def isUnique(self, word):
        if word == '': return True
        key = self.encoder(word)
        if not self.d.get(key):
            return True
        else:
            if word in self.d[key] and len(self.d[key])==1:
                return True
        return False

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param = obj.isUnique(word)