class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set)
        self.tweetMap = defaultdict(list)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweetMap: self.tweetMap[userId] = []
        self.tweetMap[userId].append((self.count, tweetId))
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []

        self.followMap[userId].add(userId)

        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                tweetCnt, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(heap, (tweetCnt, tweetId, followeeId , index - 1))

        tweets = []

        while heap and len(tweets) < 10:
            _, tweetId, follower, tweetIndex = heapq.heappop(heap)
            tweets.append(tweetId)

            if tweetIndex < 0: continue

            followerTweets = self.tweetMap[follower]

            tweetCnt, tweetId = followerTweets[tweetIndex]
            heapq.heappush(heap, (tweetCnt, tweetId, follower, tweetIndex-1))

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)

