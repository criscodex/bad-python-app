import os
import flask
import re

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # sanitize input: allow only alphanumeric characters
    re.sub(r'[^a-zA-Z0-9]', '', route_param)
    
    # ruleid:dangerous-os-exec
    os.execl("/bin/bash", "/bin/bash", "-c", route_param)

    return "oops!"


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok:dangerous-os-exec
    os.execl("static")

    return "ok!"
