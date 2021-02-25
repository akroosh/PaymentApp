from app import db


class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Integer)
    description = db.Column(db.Text, default=None)
    field = db.Column(db.Integer)
