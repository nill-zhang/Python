#!/usr/bin/python
# by sfzhang 2016.12.23
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import required
import flask
import time
from datetime import datetime


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = "SHAOFENG ZHANG"


class UserForm(Form):
    name = StringField("What is your name?", validators=[required()])
    submit = SubmitField("Submit")


@app.route("/", methods=["GET", "POST"])
def handler1():
    web_name = flask.current_app.name
    base_url = flask.request.base_url
    request_host = flask.request.host
    browser_type = flask.request.headers.get("User-Agent")
    request_method = flask.request.method

    # Solution 1
    # user_form = UserForm()
    # user_name = None
    # print("Before Submitting!")
    # if user_form.validate_on_submit():
    #     user_name = user_form.name.data
    #     # clear name field
    #     user_form.name.data = "input something here"
    # return flask.render_template("index.html",
    #                              u_form=user_form, u_name=user_name,
    #                              w_name=web_name,
    #                              b_url=base_url,
    #                              r_host=request_host,
    #                              b_type=browser_type,
    #                              r_method=request_method)

    # Solution 1 Improved version to counter refresh the page
    # and double posts
    user_form = UserForm()
    print("user_form.data: %s" % user_form.data)
    print("Before Submitting!!")
    if user_form.validate_on_submit():
        flask.session["u_name"] = user_form.name.data
        flask.flash("Good job! %s" % user_form.name.data, "info")
        flask.flash("Good job! Wahaha!", "info")
        flask.flash("Good job! Horaay!", "info")
        flask.flash("%s" % time.asctime(time.localtime(time.time())), "info")
        return flask.redirect(flask.url_for("handler1"))

    return flask.render_template("index.html",
                                 u_form=user_form, u_name=flask.session.get("u_name"),
                                 w_name=web_name,
                                 b_url=base_url,
                                 r_host=request_host,
                                 b_type=browser_type,
                                 r_method=request_method)


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



