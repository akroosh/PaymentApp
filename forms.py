from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, SelectField, HiddenField, FloatField
from wtforms.validators import DataRequired
from models import Currency

class BillForm(FlaskForm):
    amount = FloatField("Amount: ", validators=[DataRequired()])
    currency = SelectField("Currency: ", choices=Currency.query.all())
    description = TextAreaField("Goods description: ", validators=[DataRequired()])
    #shop_id = HiddenField()
    #shop_order_id = HiddenField()
    #sign = HiddenField()
    submit = SubmitField("Submit")

    def __init__(self, *args, **kwargs):
        super(BillForm, self).__init__(*args, **kwargs)
        #self.shop_id = 5
        #self.sign = 'e2801020e14cdc6769c807ace4c291b9090836742587ec8537df400fa2de36fc'
        #self.shop_order_id = 30
