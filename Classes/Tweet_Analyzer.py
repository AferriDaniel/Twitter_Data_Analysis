import tweepy as tp
class Tweet_Analyzer:
    def __init__(self, api_key, consumer_secret,access_token, access_token_secret):
        self.api_key = api_key
        self.consumer_secret = consumer_secret
        self.access_token = access_token
        self.access_token_secret = access_token_secret
        self.auth = tp.OAuthHandler(self.api_key,self.consumer_secret)
        self.auth.set_access_token(self.access_token,self.access_token_secret)
        self.api = tp.API(self.auth,wait_on_rate_limit = True, wait_on_rate_limit_notify = True)


    def login(self):
        try:
            self.api.verify_credentials()
            print('Logeado!')
        except:
            print('No Logeado :(')

   # def collect_tweets(self, search_words,count, until ,size):
   #     return tp.Cursor(self.api.search, q = search_words, count = count, until = until ).items(size)

    # def get_tweets_ids(self, tweets):
    #    return [tweet.id for tweet in tweets]

    def public_tweets(self):
        tweets = self.api.home_timeline()
        return [tweet.text for tweet in tweets]

if __name__ == '__main__':


    api_key = 'rxoUGqDngwTYobqzvMyWYFsBW'
    consumer_secret = 'e6g7KCN88tEOf1haB8zfNEHhiF9RWOnx07uaDmTUYGLypDXDIE'
    access_token = '2162259074-ZPVbjEZ0RSC8Tg97xrd5hDk3sXM7iS9TRSTNmBR'
    access_token_secret = 'EWPn4N07UP38hYYo7Eif7CwvsWa2d3YuBH8qOHk8qV5gx'

    twitter_summary = Tweet_Analyzer(api_key,consumer_secret,access_token,access_token_secret)
    twitter_summary.login()
    twitter_summary.public_tweets()
    