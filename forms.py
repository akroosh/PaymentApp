from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired
from models import Currency

class BillForm(FlaskForm):
    amount = IntegerField("Amount: ", validators=[DataRequired()])
    currency = SelectField("Currency: ", choices=Currency.query.all())
    description = TextAreaField("Goods description: ", validators=[DataRequired()])
    submit = SubmitField("Submit")