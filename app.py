import flask
app = flask.Flask(__name__)

tweets = [1,2,3,4,5]


@app.route('/')
def index():
    return flask.render_template('home.html', tweets_count = len(tweets))

@app.route('/about')
def about():
    return flask.render_template('about.html')

@app.route("/signup/")
def show_signup_form():
    return flask.render_template("user_info_form.html")

if __name__ == '__main__':
    app.run(debug = True)


