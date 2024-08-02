class Twitter:
    def __init__(self):
        self.time = 0

        # Tweets contains userId -> [(timestamp, tweetId)]
        self.tweets = defaultdict(list)

        # Follows contains a set userId -> [userId]
        # Uses a set because elements must be unique
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time -= 1  # Since we need a max heap

    def getNewsFeed(self, userId: int) -> List[int]:
        userIds = [userId]
        tweets = []
        res = []
        for uid in self.follows[userId]:
            userIds.append(uid)

        for uid in userIds:
            for tweet in self.tweets[uid]:
                tweets.append(tweet)

        heapq.heapify(tweets)
        while len(tweets) > 0 and len(res) < 10:
            tweet = heapq.heappop(tweets)[1]
            res.append(tweet)

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
