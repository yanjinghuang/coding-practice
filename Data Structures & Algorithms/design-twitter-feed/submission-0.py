class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)
        self.time = 0
        self.n = 10 

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        if len(self.tweetMap[userId]) > self.n:
            self.tweetMap[userId].pop(0)
        self.time -= 1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        minHeap = []
        self.followMap[userId].add(userId)
        if len(self.followMap[userId]) >= self.n:
            maxHeap = []
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    time, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(maxHeap,[-time, tweetId, followeeId, index-1])

                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            
            while maxHeap:
                time, tweetId, followeeId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap,[-time, tweetId, followeeId, index])

        else:
            for followeeId in self.followMap[userId]:
                if followeeId in self.tweetMap:
                    index = len(self.tweetMap[followeeId]) - 1
                    time, tweetId = self.tweetMap[followeeId][index]
                    heapq.heappush(minHeap,[time, tweetId, followeeId, index-1])
        
        while minHeap and len(res) < self.n:
            time, tweetId, followeeId, index = heapq.heappop(minHeap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush(minHeap,[time, tweetId, followeeId, index-1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
        
