import os
import praw
from datetime import datetime

# Remplace ces valeurs avec tes vraies clés API
reddit = praw.Reddit(
    client_id=os.environ["REDDIT_CLIENT_ID"],
    client_secret=os.environ["REDDIT_CLIENT_SECRET"],
    user_agent=os.environ.get("REDDIT_USER_AGENT", "tennis-sentiment-analysis")
)


def get_reddit_comments(query, limit=50, year=None):
    results = []
    subreddit = reddit.subreddit("tennis")

    for submission in subreddit.search(query, sort="new", limit=limit*2):
        if year:
            try:
                post_year = datetime.utcfromtimestamp(submission.created_utc).year
                if post_year != year:
                    continue
            except:
                continue

        submission.comments.replace_more(limit=0)
        for comment in submission.comments[:10]:
            comment_year = datetime.utcfromtimestamp(comment.created_utc).year
            if year and comment_year != year:
                continue
            results.append({
                "text": comment.body,
                "date": datetime.utcfromtimestamp(comment.created_utc).date()
            })
            if len(results) >= limit:
                return results
    return results
