#!/usr/bin/python
# by sfzhang 2016.12.23
from flask_script import Manager
import flask
import sys


app = flask.Flask(__name__)


@app.route("/")
def handler1():
    return """<h1>This is sfzhang's homepage</h1>
              <br>Webpage name: %s</br><br>Base_Url: %s</br>
              <br>date: %r</br><br>Host: %s</br><br>Browser: %s</br>
              <br>Request Method: %s</br>
              """ % \
             (flask.current_app.name, flask.request.base_url,
              flask.request.date, flask.request.host,
              flask.request.headers.get("User-Agent"),flask.request.method)


@app.route("/<username>")
def handler2(username):
    return "<h1>%s, welcome to SFZHANG.COM" % username


@app.route("/forbidden")
def handler3():
    return "<h1>Page Forbidden by Server</h1>", 403


@app.route("/response")
def handler4():
    response = flask.make_response("<h2>This Documents Carries a cookie</h2>")
    response.set_cookie("answer", "42")
    return response


@app.route("/internal_redirect")
def handler5():
    return flask.redirect("external_redirect")


@app.route("/external_redirect")
def handler6():
    # must come with scheme, otherwise
    # flask will consider it as a internal link
    return flask.redirect("http://www.google.com")


@app.route("/<int:uid>")
def handler7(uid):
    user = load_user(uid)
    if not user:
        flask.abort(404)
    return "<h1>Hi, %s</h1>" % user


@app.route('/hello/<string:login_name>')
def hello(login_name=None):
    return flask.render_template("login.html", what_name=login_name)


@app.route("/profile/<string:name>")
def show_profile(name):
    return flask.render_template('profile.html', name=name)


def load_user(user_id):
    users = {100: "sfzhang", 101: "xlyang", 102: "lyzhang"}
    return users.get(user_id)  #default to none if key is not found

if __name__ == "__main__":
    # app.run(debug=True)
    # app = Manager(app)
    # if len(sys.argv) == 1:
    #     sys.argv.extend(["runserver", "--host", "0.0.0.0"])
    app.run()



