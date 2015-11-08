import flask
app = flask.Flask(__name__)


@app.route("/")
def mainpage():
    return "Wassup Noobs, u finna get PK'd by Joe and Sid?"

if __name__ == "__main__":
    app.run(port=80)
    print "hello world"
