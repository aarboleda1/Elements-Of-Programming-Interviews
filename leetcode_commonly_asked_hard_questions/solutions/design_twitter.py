from datetime import datetime
from heapq import heappop, heappush
from typing import List
from collections import defaultdict


"""This implementation requires creating a graph in which
users can follow and unfollow each other. The ultimate goal
is to get a newsFeed.

If you work backwards from this, you'll see that the
most recently added tweets will be merge K sorted lists whether
they be arrays or linked lists of the 10 most recent stamps

Let's first design what a basic design would be. Since it is a social graph,
we'll firstly need a User object, which will hold a list of tweets and following
ids

Now, when we follow, post, or unfollow, we can use the user hash map to determine


target = 100, A = [1,30]
100 - 30 = 70
"""
"""
Twitter API Design

User:
    tweets
    following

Twitter:
    id_to_user_map



Attempt Log
- 5/4
"""
class Tweet:
    def __init__(self, id):
        self.timestamp = datetime.now()
        self.id = id


class User:
    def __init__(self, uid, tweets=None):
        self.uid = uid
        self.tweets = tweets or []
        self.followees = defaultdict(User)

    def addTweet(self, tweet):
        self.tweets.append(tweet)

    def addFollowee(self, followee):
        # follow a person
        self.followees[followee.uid] = followee

    def removeFollowee(self, followee):
        if followee.uid in self.followees:
            del self.followees[followee.uid]


class UserGraph:
    def __init__(self):
        self.users = {}  # Dict[id, User]

    def follow(self, followerId, followeeId):
        if followeeId not in self.users:
            self.users[followeeId] = User(followeeId)
        follower = self.users.get(followerId)
        follower.addFollowee(self.users[followeeId])


    def unfollow(self, followerId, followeeId):
        if followerId not in self.users or followeeId not in self.users:
            return
        self.users[followerId].removeFollowee(self.users[followeeId])

    def getUser(self, uid):
        if uid not in self.users:
            self.users[uid] = User(id)
        return self.users.get(uid)


class Twitter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.userGraph = UserGraph()

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        user = self.userGraph.getUser(userId)
        newTweet = Tweet(tweetId)
        user.addTweet(newTweet)

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        k, newsFeed = 10, []
        user = self.userGraph.getUser(userId)
        self._getKMostTweets(user.tweets, k, newsFeed)
        for followee in user.followees.values():
            self._getKMostTweets(followee.tweets, k, newsFeed)
        return [tweet.id for tweet in newsFeed]

    def _getKMostTweets(self, tweets, size, newsFeed):
        for tweet in tweets:
            heappush(newsFeed, tweet)
            if len(newsFeed) > size:
                heappop(newsFeed)
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.userGraph.follow(followerId, followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.userGraph.unfollow(followerId, followeeId)

# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------

"""SOLUTION 2
"""

class Twitter_V2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # user -> List[Tuple(int, int)] users to tweets of time and tweetId
        self.tweets = {}
        # follower -> List[int]
        self.followees = {}
        self.time = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.tweets[userId] = self.tweets.get(userId, []) + [(self.time, tweetId)]
        self.time += 1

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        heap, tweets = [], self.tweets
        followees = self.followees.get(userId, set()) | set([userId])
        for followeeId in followees:
            if followeeId in tweets and tweets[followeeId]:
                time, tweetId = tweets[followeeId][-1]
                heappush(heap, (-time, tweetId, followeeId, len(tweets[followeeId]) - 1))
        newsFeed = []
        for _ in range(10):
            if heap:
                time, tweetId, followeeId, idx = heappop(heap)
                newsFeed.append(tweetId)
                if idx > 0: # they have more tweets
                    newTime, newTweetId = self.tweets[followeeId][idx - 1]
                    heappush(heap, (-newTime, newTweetId, followeeId, idx - 1))

        return newsFeed

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        self.followees[followerId] =  self.followees.get(followerId, set()) | set([followeeId])


    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.followees:
            self.followees[followerId].discard(followeeId)


if __name__ == "__main__":
    twitter = Twitter()
    # User 1 posts a new tweet (id = 5).
    twitter.postTweet(1, 5)

    # User 1's news feed should return a list with 1 tweet id -> [5].
    print(twitter.getNewsFeed(1))
    assert twitter.getNewsFeed(1) == [5]

    # User 1 follows user 2.
    twitter.follow(1, 2)

    # User 2 posts a new tweet (id = 6).
    twitter.postTweet(2, 6)

    # User 1's news feed should return a list with 2 tweet ids -> [6, 5].
    # Tweet id 6 should precede tweet id 5 because it is posted after tweet id 5.
    print(twitter.userGraph.getUser(1).followees)
    assert twitter.getNewsFeed(1) == [6, 5]

    # User 1 unfollows user 2.
    twitter.unfollow(1, 2)

    # User 1's news feed should return a list with 1 tweet id -> [5],
    # since user 1 is no longer following user 2.
    assert twitter.getNewsFeed(1) == [5]
