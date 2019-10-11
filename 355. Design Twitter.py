'''
Title     : 355. Design Twitter
Problem   : https://leetcode.com/problems/design-twitter/description/s
'''
''' Reference: https://leetcode.com/problems/design-twitter/discuss/131998/Python-no-heap-easy-and-clear-solution-68-ms-beats-100 '''
import collections
class Twitter(object):

    def __init__(self):
        self.tweets = collections.defaultdict(list)
        self.following = collections.defaultdict(set)
        self.order = 0
        
    def postTweet(self, userId, tweetId):
        self.tweets[userId] += (self.order, tweetId),   # , to convert non-iterable int to iterable tuple
        self.order -= 1

    def getNewsFeed(self, userId):
        tmp = []
        for Id in self.following[userId] | {userId}:   # union to include the user him/herself
            for t in self.tweets[Id]:
                tmp.append(t)
        tw = sorted(tmp)[:10]
        # one-liner: tw = sorted(t for Id in self.following[userId] | {userId} for t in self.tweets[Id])[:10]
        return [news for _, news in tw]

    def follow(self, followerId, followeeId):
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.following[followerId].discard(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)