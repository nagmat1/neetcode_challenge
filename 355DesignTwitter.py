class Twitter:


    def __init__(self):
        self.user = defaultdict(set)
        self.tweet = deque() 
      

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet.appendleft((userId,tweetId))
      
    def getNewsFeed(self, userId: int) -> List[int]:
        res = [] 
        for user,tweetId in self.tweet:
            if userId == user or user in self.user[userId]: 
                res.append(tweetId)
        return res[:10]
        #return [tweetId for user, tweetId in self.tweet if userId == user or user in self.user[userId]][:10]
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user[followerId].discard(followeeId)
