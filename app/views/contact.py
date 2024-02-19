from flask import Blueprint, render_template
import lorem

from app.extensions.mail import mail
from app.forms.contact import Contact

contact = Blueprint("contact", __name__)


@contact.route("/", methods=["GET", "POST"])
def index():
    contact_form = Contact()

    if contact_form.validate_on_submit():
        mail.send_message(
            f"Contact - {contact_form.name.data}",
            ["contact@mewi.dev"],
            f"Hello, {contact_form.name.data} ({contact_form.email.data}) would like to get in touch!\n\n{contact_form.message.data}"
        )
        return render_template(
            "contact/index.html",
            message_is_sent=True
        )

    return render_template(
        "contact/index.html",
        message_is_sent=False,
        contact_form=contact_form,
        lorem_text=lorem.paragraph()
    )
