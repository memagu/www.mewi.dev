from flask import Blueprint, render_template

about = Blueprint("about", __name__)


@about.route("/")
def index():
    return render_template("about/index.html")
