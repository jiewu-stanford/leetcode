'''
Title     : 269. Alien Dictionary ($$$)
Problem   : https://leetcode.com/problems/alien-dictionary/description/
          : https://www.lintcode.com/problem/alien-dictionary/description (one test case ['zy', 'zx'] is wrong)
'''
'''
as illustrated by the example, compare adjacant pair of words and store predecessor-successor order for distinct characters
Reference: https://medium.com/@dimko1/alien-dictionary-6cf2da24bf3c
'''
import collections
class Solution:
    def alienOrder(self, words):
        pre = collections.defaultdict(set)
        suc = collections.defaultdict(set)
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    suc[a].add(b);  pre[b].add(a)
                    break   # break because we can only be certain about the order of the first pair of distinct characters

        chars = set(''.join(words))
        zeroInDeg = chars - set(pre)
        res = []
        while zeroInDeg:
            c = zeroInDeg.pop()
            res.append(c)
            for a in suc[c]:
                pre[a].discard(c)   # remove the predecessor c to check whether a becomes new zero in-degree node
                if not pre[a]:
                    zeroInDeg.add(a)
            del suc[c]
        return ''.join(res) if set(res)==chars else ''
'''
more general (any word pair) helper function to determine predecessors and successors and use successor dictionary to check whether all characters have been visited
Reference: https://www.cnblogs.com/lightwindy/p/8531872.html
'''
class Solution:
    def alienOrder(self, words):
        pre, suc = {}, {}
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                return ''   # no pair of distinct characters found
            self.predsuccessor(words[i-1], words[i], pre, suc)
            
        chars = set(''.join(words))
        zeroInDeg = chars - set(pre)
        res = []
        while zeroInDeg:
            c = zeroInDeg.pop()
            res.append(c)
            if c in suc:
                for a in suc[c]:
                    pre[a].discard(c)
                    if not pre[a]:
                        zeroInDeg.add(a)
                del suc[c]
        return ''.join(res) if not suc else ''
        
    def predsuccessor(self, word1, word2, pre, suc):
        l = min(len(word1), len(word2))
        for i in range(l):
            if word1[i] != word2[i]:
                if word2[i] not in pre:
                    pre[word2[i]] = set()
                    pre[word2[i]].add(word1[i])
                if word1[i] not in suc:
                    suc[word1[i]] = set()
                    suc[word1[i]].add(word2[i])
                break
'''
DFS solution using recursive helper function to check the existence of cycle, if no then DFS can complete the ordering, ibid.
it produces different results from the above two solutions for words like ['zy', 'zx'] that have to determine order from a single word (e.g. 'zy' for 'z' < 'y')
'''
class Solution:
    def alienOrder(self, words):
        pre, visited = {}, {}
        chars = set(''.join(words))
        for c in chars: pre[c] = set()   # have to initialize, otherwise RTE in isCyclic
        for i in range(1, len(words)):
            if len(words[i-1]) > len(words[i]) and words[i-1][:len(words[i])] == words[i]:
                return ''
            self.predsuccessor(words[i-1], words[i], pre)
            
        res = []
        for c in chars:
            if self.isCyclic(c, c, pre, visited, res):
                return ''
        return ''.join(res)        

    def predsuccessor(self, word1, word2, pre):
        l = min(len(word1), len(word2))
        for i in range(l):
            if word1[i] != word2[i]:
                pre[word2[i]].add(word1[i])
                break

    def isCyclic(self, root, node, predecessors, visited, res):
        if node not in visited:
            visited[node] = root   # starting node of the traversal
            for p in predecessors[node]:
                if self.isCyclic(root, p, predecessors, visited, res):
                    return True
            res.append(node)
        elif visited[node] == root:   # visit again in current traversal, cycle detected
            return True
        return False