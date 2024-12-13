


import praw
from datetime import datetime, timedelta

# Initialize the Reddit client
reddit = praw.Reddit(
    client_id="your client id",
    client_secret="your seceret id",
    user_agent="username"
)

# Function to extract comments from the last 'x' days
def fetch_recent_comments(subreddit_name, days):
    subreddit = reddit.subreddit(subreddit_name)
    recent_comments = []
    author_names = []  
    cutoff_time = datetime.utcnow() - timedelta(days=days)
    
    for i in subreddit.comments(limit=10000):  # Limit you adjust as needed but mind that reddit api restrict it based on rate limits
        comment_time = datetime.utcfromtimestamp(i.created_utc)
        if comment_time > cutoff_time:
            # Add comment details
            recent_comments.append({
                "author": str(i.author),  # Store author's name
                "body": i.body,
                "created_utc": comment_time.strftime('%Y-%m-%d %H:%M:%S'),
                "permalink": f"https://www.reddit.com{i.permalink}"
            })
            # Add author name to the separate list
            author_names.append(str(i.author))
    
    return recent_comments, author_names

# Example usage
subreddit_name = "subredditname"  # Replace with your  subreddit
days=int(input("enter the no. of x days"))
comments, author_names = fetch_recent_comments(subreddit_name,days)

# Output comments and author names
if comments:
    print("Recent Comments:")

    for comment in comments:
             print(f"Author: {comment['author']}")
             print(f"Comment: {comment['body']}")
             print(f"Posted at: {comment['created_utc']}")
             print(f"Link: {comment['permalink']}")
             print("-" * 80)
else:
    print("No comments found in the specified timeframe.")
# To count the occurence of each author
d={}
for i in author_names:
    if i in d:
        d[i]+=1
    else:
        d[i]=1


sorted_desc_values = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
print(sorted_desc_values)