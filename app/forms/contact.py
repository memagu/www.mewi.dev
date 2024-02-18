from flask_wtf import FlaskForm
import wtforms
from wtforms.validators import DataRequired, Email


class Contact(FlaskForm):
    name = wtforms.StringField("Name", validators=(DataRequired(),))
    email = wtforms.EmailField("Email address", validators=(DataRequired(), Email()))
    message = wtforms.TextAreaField("Message", validators=(DataRequired(),))
    submit = wtforms.SubmitField("Submit")
