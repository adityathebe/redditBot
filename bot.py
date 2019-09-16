import os
import praw
import time
import requests as request

from config import REDDIT_PASSWORD, REDDIT_USERNAME, REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
from config import STREAMABLE_USER, STREAMABLE_PASS
from config import SUBREDDITS, VALID_DOMAINS

reddit = praw.Reddit(
    user_agent='u/' + REDDIT_USERNAME + 'v1.0',
    username=REDDIT_USERNAME,
    password=REDDIT_PASSWORD,
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET
)


def replyLink(video_url):
    STREAM_API = 'https://api.streamable.com/import?url='
    reply = '###[Streamable Mirror](https://streamable.com/{})'
    api_query_url = (STREAM_API+video_url).strip()
    r = request.get(api_query_url, auth=(STREAMABLE_USER, STREAMABLE_PASS))
    if r.status_code == 200:
        shortcode = r.json()['shortcode']
        return reply.format(shortcode)
    return None


def getStreams():
    start_time = time.time()
    print('Streaming new submissions ...')
    for sub in reddit.subreddit(SUBREDDITS).stream.submissions():
        if sub.created_utc < start_time:
            continue  # Ignore old messages

        print('\n\n{}\n- By {} on {}'.format(
            sub.title,
            sub.author,
            sub.subreddit_name_prefixed
        ))

        if sub.domain not in VALID_DOMAINS:
            continue

        stremable_video_url = replyLink(sub.url)
        if stremable_video_url:
            sub.reply(stremable_video_url)
            print('- Replied succesfully')
        else:
            print('- Submission is not a video')


if __name__ == '__main__':
    getStreams()
