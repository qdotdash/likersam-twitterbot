from re import search
import tweepy
import time

from tweepy.error import TweepError
from tweepy.models import SearchResults

auth = tweepy.OAuthHandler('a', 'b')
auth.set_access_token('c', 'd')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
userme = api.me()

# search = 'power of habit'
# nrTweets = 500

# for tweet in tweepy.Cursor(api.search, search).items(nrTweets):
#     try:
#          print('Tweet Liked')
#          tweet.favorite()
#          time.sleep(10)
#     except tweepy.TweepError as e:
#         print(e.reason)
#     except StopIteration:
#         break

userID = "randomid"
user = api.get_user(userID)

tweets = api.user_timeline(screen_name=userID, 
                           # 200 is the maximum allowed count
                           count=200,
                           include_rts = False,
                           # Necessary to keep full_text 
                           # otherwise only the first 140 words are extracted
                           tweet_mode = 'extended',
                           exclude_replies=True,
                           )

# print(tweets[0].in_reply_to_user_id)
i = 1
for tweet in tweets:
    try:
        api.create_favorite(tweet.id)
        print(tweet.full_text, tweet.in_reply_to_user_id, i)
        i += 1
        #  tweet.favorite()
        # time.sleep(10)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break