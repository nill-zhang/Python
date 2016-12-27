#!/usr/bin/python
# by sfzhang 2016.12.23
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
import flask
from datetime import datetime


app = flask.Flask(__name__)


@app.route("/")
def handler1():
    return """<h1>This is sfzhang's homepage</h1>
              <br>Webpage Name: %s</br>
              <br>Base_Url: %s</br>
              <br>Host: %s</br>
              <br>Browser: %s</br>
              <br>Request Method: %s</br>
              """ % \
             (flask.current_app.name,
              flask.request.base_url,
              flask.request.host,
              flask.request.headers.get("User-Agent"),
              flask.request.method,
              )


@app.route("/<username>")
def handler2(username):
    return "<h1>%s, welcome to SFZHANG.COM" % username


@app.route("/forbidden")
def handler3():
    return "<h1> %s , Page Forbidden by Server</h1>" % flask.url_for("handler3", _external=True), 403


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
    current_time = datetime.utcnow()
    return flask.render_template("login.html", display_name=login_name,
                                 current_time=current_time)


@app.route("/profile/<string:name>")
def show_profile(name):
    return flask.render_template('profile.html', name=name)


def load_user(user_id):
    users = {100: "sfzhang", 101: "xlyang", 102: "lyzhang"}
    return users.get(user_id)  # default to none if key is not found


@app.errorhandler(404)
def page_not_found(e):  # Note: error handling function has e argument
    # Note that, here you can put url_for directly in 404.html as a
    # placeholder, or you generate the link and use it to substitute an
    # variable in 404.html like the following commented part
    # link = flask.url_for("static", filename="page_not_found.jpg")
    # return flask.render_template("404.html", link=link), 404
    return flask.render_template("404.html"), 404


@app.errorhandler(500)
def server_error(e):
    return flask.render_template("500.html"), 500


if __name__ == "__main__":
    # app.run(debug=True)
    # app = Manager(app)
    # if len(sys.argv) == 1:
    #     sys.argv.extend(["runserver", "--host", "0.0.0.0"])
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    app.run()



