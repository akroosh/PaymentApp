from app import db
from hashlib import sha256
import json


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currency_id = db.Column(db.Integer, db.ForeignKey('currency.id'), nullable=False)
    amount = db.Column(db.Float)
    description = db.Column(db.Text, default=None)
    shop_id = db.Column(db.Integer, default=5)
    payway = db.Column(db.String(50), default='payway_rub')

    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.shop_id = 5

    def __repr__(self):
        return f'{self.description=} {self.amount=}'

    @property
    def sign(self):
        # secret mae buty in env
        secret = 'SecretKey01'
        ########!!!!!!!!!
        sign = f'{self.amount}:{self.currency.code}:{self.payway}:{self.shop_id}:{self.id}{secret}'
        return sha256(sign.encode('utf-8')).hexdigest()

    @property
    def json(self):
        return json.dumps({
            "currency": self.currency.code,
            "sign": self.sign,
            "payway": self.payway,
            "amount": self.amount,
            "shop_id": self.shop_id,
            "shop_order_id": self.id,
            "payer_currency": self.currency.code,
            "shop_amount": self.amount,
            "shop_currency": self.currency.code,
        })


class Currency(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.Integer)
    name = db.Column(db.String(5))
    order = db.relationship('Order', backref='currency', lazy=True)

    def __init__(self, *args, **kwargs):
        super(Currency, self).__init__(*args, **kwargs)

    def __repr__(self):
        return f'{self.name}'
