import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

def fetch_reddit_posts(subreddit="MachineLearning", limit=5):
    posts = []
    for submission in reddit.subreddit(subreddit).hot(limit=limit):
        posts.append({
            "title": submission.title,
            "selftext": submission.selftext,
            "url": submission.url
        })
    return posts

if __name__ == "__main__":
    print(fetch_reddit_posts("MachineLearning"))
