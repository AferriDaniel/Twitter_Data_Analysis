import flask
app = flask.Flask(__name__)


@app.route('/')
def index():
    return 'This is my twitter data analysis project'
if __name__ == '__main__':
    app.run(debug = True)

