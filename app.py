import flask
from Classes.Tweet_Analyzer import Tweet_Analyzer


app = flask.Flask(__name__)


api_key = 'ENTER YOUR CREDENTIALS HERE'
consumer_secret = 'ENTER YOUR CREDENTIALS HERE'
access_token = 'ENTER YOUR CREDENTIALS HERE'
access_token_secret = 'ENTER YOUR CREDENTIALS HERE'

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
