import flask
from Classes.Tweet_Analyzer import Tweet_Analyzer


app = flask.Flask(__name__)


api_key = 'rxoUGqDngwTYobqzvMyWYFsBW'
consumer_secret = 'e6g7KCN88tEOf1haB8zfNEHhiF9RWOnx07uaDmTUYGLypDXDIE'
access_token = '2162259074-ZPVbjEZ0RSC8Tg97xrd5hDk3sXM7iS9TRSTNmBR'
access_token_secret = 'EWPn4N07UP38hYYo7Eif7CwvsWa2d3YuBH8qOHk8qV5gx'

twitter_summary = Tweet_Analyzer(api_key,consumer_secret,access_token,access_token_secret)


@app.route('/')
def index():
    return flask.render_template('home.html', tweets_count = len(twitter_summary.public_tweets()))

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route("/signup/")
def show_signup_form():
    return flask.render_template("user_info_form.html")
if __name__ == '__main__':
    app.run(debug = True)