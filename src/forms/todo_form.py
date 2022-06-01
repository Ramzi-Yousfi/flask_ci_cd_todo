from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField,EmailField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length


class TodoForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[Length(min=0, max=140)])
    done = BooleanField('Done')
    submit = SubmitField('Submit')