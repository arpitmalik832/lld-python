from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List


@dataclass
class SocialMediaPost:
    id: str
    status: str
    user_id: int
    timestamp: int


@dataclass
class FacebookPost:
    id: str
    status: str
    user_id: int
    timestamp: int


@dataclass
class TwitterTweet:
    id: str
    tweet: str
    user_id: int


# External Facebook API
class FacebookApi:
    def fetch_facebook_posts(
        self, user_id: int, timestamp: int
    ) -> List["FacebookPost"]:
        # Implementation to fetch Facebook posts
        return [FacebookPost("1", "Hello World", 1, 123456789)]

    def post_facebook_status(self, user_id: int, status: str) -> None:
        # Implementation to post a status on Facebook
        pass


# External Twitter API
class TwitterApi:
    def get_tweets(self, user_id: int) -> List["TwitterTweet"]:
        # Implementation to fetch Twitter tweets
        return [TwitterTweet("1", "Hello World", 1)]

    def tweet(self, user_id: int, text: str) -> None:
        # Implementation to send a tweet on Twitter
        pass


class SocialMediaAdapter(ABC):
    @abstractmethod
    def fetch_posts(self, user_id: int, timestamp: int) -> List[SocialMediaPost]:
        pass

    @abstractmethod
    def add_post(self, user_id: int, status: str) -> None:
        pass


class FacebookAdapter(SocialMediaAdapter):
    def __init__(self):
        self.__api = FacebookApi()

    def fetch_posts(self, user_id: int, timestamp: int) -> List[SocialMediaPost]:
        posts = self.__api.fetch_facebook_posts(user_id, timestamp)

        result = []
        for post in posts:
            result.append(
                SocialMediaPost(post.id, post.status, post.user_id, post.timestamp)
            )
        return result

    def add_post(self, user_id: int, status: str) -> None:
        self.__api.post_facebook_status(user_id, status)


class TwitterAdapter(SocialMediaAdapter):
    def __init__(self):
        self.__api = TwitterApi()

    def fetch_posts(self, user_id: int, timestamp: int) -> List[SocialMediaPost]:
        posts = self.__api.get_tweets(user_id)

        result = []
        for post in posts:
            result.append(SocialMediaPost(post.id, post.tweet, post.user_id, 0))
        return result

    def add_post(self, user_id: int, status: str) -> None:
        self.__api.tweet(user_id, status)


class SocialMediaManager:
    def __init__(self):
        self.facebook_api = FacebookApi()
        self.twitter_api = TwitterApi()

    def get_messages(self, user_id: int, timestamp: int, platform: str):
        if platform == "facebook":
            posts: List[FacebookPost] = self.facebook_api.fetch_facebook_posts(
                user_id, timestamp
            )
        elif platform == "twitter":
            tweets: List[TwitterTweet] = self.twitter_api.get_tweets(user_id)
        else:
            raise ValueError("Invalid platform specified")
