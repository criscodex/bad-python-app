import os
import flask
from shlex import join

app = flask.Flask(__name__)


@app.route("/route_param/<route_param>")
def route_param(route_param):

    # use shlex functions to correctly parse the command-line arguments
    new_route = join(["/bin/bash", "-c", route_param])

    # ruleid:dangerous-os-exec
    os.execl("/bin/bash", new_route)

    return "oops!"


# Flask true negatives
@app.route("/route_param/<route_param>")
def route_param2(route_param):

    # ok:dangerous-os-exec
    os.execl("static")

    return "ok!"
