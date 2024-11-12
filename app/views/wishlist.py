from flask import Blueprint, render_template

wishlist = Blueprint("wishlist", __name__)


@wishlist.route("/")
def index():
    return render_template("wishlist/index.html")