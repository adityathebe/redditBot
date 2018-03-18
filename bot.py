import requests as request
import praw, os

reddit = praw.Reddit(
    user_agent = 'u/botlimbu v1.0',
    client_id = os.environ.get('CLIENT_ID'),
    client_secret = os.environ.get('CLIENT_SECRET'),
    username= os.environ.get('USERNAME'),
    password= os.environ.get('PASSWORD')
)

VALID_DOMAINS = [ 
    'twitter.com', 'instagram.com', 'facebook.com', 
    'imgtc.com', 'imgtc.b-cdn.net', 'clippituser.tv'
]

subreddit = reddit.subreddit('gunners+MCFC+chelseafc+LiverpoolFC')

def replyLink(sub):
    STREAM_API = 'https://api.streamable.com/import?url=';
    reply = '###[Streamable Mirror](https://streamable.com/{})'
    user = os.environ['STREAM_USER']
    password = os.environ['STREAM_PASS']

    video_url = (STREAM_API+sub.url).strip()
    r = request.get(video_url, auth=(user, password) )
    if(r.status_code == 200):
        shortcode = r.json()['shortcode']
        return reply.format(shortcode)
    return 'not-video'

def getStreams():
    count = 0
    for sub in subreddit.stream.submissions():
        count += 1
        if (count > 100):   # Exclude the first 100 previous submissions
            if sub.domain in VALID_DOMAINS:
                data = replyLink(sub)
                if(data != 'not-video'):
                    sub.reply(data)
                    print('{} . {}'.format(count, sub.title))

getStreams()