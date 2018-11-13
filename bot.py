import requests as request
import praw
import os

reddit = praw.Reddit(
    user_agent='u/botlimbu v1.0',
    username=os.environ.get('USERNAME'),
    password=os.environ.get('PASSWORD'),
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET')
)

VALID_DOMAINS = [
    'twitter.com', 'instagram.com', 'facebook.com',
    'imgtc.com', 'imgtc.b-cdn.net', 'clippituser.tv'
]

subreddit = reddit.subreddit('botlimbu+gunners+MCFC+chelseafc+LiverpoolFC')


def replyLink(sub):
    STREAM_API = 'https://api.streamable.com/import?url='
    reply = '###[Streamable Mirror](https://streamable.com/{})'
    user = os.environ.get('STREAM_USER')
    password = os.environ.get('STREAM_PASS')

    video_url = (STREAM_API+sub.url).strip()
    r = request.get(video_url, auth=(user, password))
    if(r.status_code == 200):
        shortcode = r.json()['shortcode']
        return reply.format(shortcode)
    return 'not-video'


def getStreams():
    print('Streaming new submissions ...')
    count = 0
    for sub in subreddit.stream.submissions():
        count += 1
        if (count >= 100):   # Exclude the first 100 previous submissions
            if sub.domain in VALID_DOMAINS:
                data = replyLink(sub)
                if (data != 'not-video'):
                    sub.reply(data)
                    print('{} . {}'.format(count, sub.title))
                else:
                    print('Not Video')
            else:
                print(sub.domain)


getStreams()
