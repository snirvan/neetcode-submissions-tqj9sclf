class Twitter:

    def __init__(self):
        self.postCount = 0
        self.following = defaultdict(set)     
        self.feed = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append([self.postCount,tweetId])
        self.postCount -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        followees = set(self.following[userId])
        followees.add(userId)

        for followeeId in followees:
            if self.feed[followeeId]:
                index = len(self.feed[followeeId]) - 1
                count, tweetId = self.feed[followeeId][index]
                heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

        while minHeap and len(res) < 10:
            count, tweetId, followeeId, nextIndex = heapq.heappop(minHeap)
            res.append(tweetId)

            if nextIndex >= 0:
                nextCount, nextTweetId = self.feed[followeeId][nextIndex]
                heapq.heappush(minHeap, [nextCount, nextTweetId, followeeId, nextIndex - 1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
            self.following[followerId].discard(followeeId)
        

#feed
#1: 10,30