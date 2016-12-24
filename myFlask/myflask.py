#!/usr/bin/python
# by sfzhang 2016.12.23
import flask
app = flask.Flask(__name__)


@app.route("/")
def handler1():
    return """<h1>hello, this is sfzhang's homepage</h1>
              <br>Webpage name: %s</br><br>Base_Url: %s</br>
              <br>date: %r</br><br>Host: %s</br><br>Browser: %s</br>
              """ % \
             (flask.current_app.name, flask.request.base_url,
              flask.request.date, flask.request.host,
              flask.request.headers.get("User-Agent"))


@app.route("/<username>/<int:userid>")
def handler2(username, uid):
    return "<h1>hello, %s, your Id: %d</h1>" % (username, uid)

def
if __name__ == "__main__":
    app.run(debug=True)

