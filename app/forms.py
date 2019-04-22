from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email


class UploadForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    firstName = StringField("First Name", validators=[DataRequired()])
    lastName= StringField("Last Name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired(), Email()])
    submit = SubmitField()
