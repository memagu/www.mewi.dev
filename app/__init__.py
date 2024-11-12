from flask import Flask

from .config import CONFIGURATIONS
from .views.home import home
from .views.about import about
from .views.contact import contact
from .views.wishlist import wishlist

from .extensions.db import db
from .extensions.mail import mail


def create_app(configuration: str = "production") -> Flask:
    app = Flask(__name__)
    app.config.from_object(CONFIGURATIONS[configuration])

    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(about, url_prefix="/about/")
    app.register_blueprint(contact, url_prefix="/contact/")
    app.register_blueprint(wishlist, url_prefix="/wishlist/")

    db.init_app(app)
    with app.app_context():
        db.create_all()

    mail.init_app(app)

    return app
