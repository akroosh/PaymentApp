from app import app, db
from flask import render_template, request, redirect, url_for
from models import Order, Currency
from forms import BillForm
import logging
import requests
import json
from abc import ABC, abstractmethod
FORMAT = '%(lineno)d %(levelname)s %(message)s'
logging.basicConfig(format=FORMAT, level=logging.DEBUG)



@app.route('/', methods=['GET', 'POST'])
def create_bill():
    '''Get data from form and redirect user to payment url.'''
    form = BillForm()

    if form.validate_on_submit():
        amount = form.amount.data
        description = form.description.data
        try:
            url = None
            currency = Currency.query.filter_by(name=form.currency.data).first()
            order = Order(amount=amount, currency_id=currency.id, description=description)
            db.session.add(order)
            db.session.commit()
            handler = Handler(order)
            url = handler.get_currency_url
        except AttributeError as e:
            logging.debug(e)
        if url:
            return redirect(url)
    return render_template('index.html', form=form)




class Handler:
    def __init__(self, order):
        self.url = None
        self.response = None
        self.order = order
        self.body = self.order.json
        self.headers = {'Content-Type': 'application/json'}

    def get_response(self, url):
        self.response = requests.post(url, self.body, headers=self.headers)

    def get_url(self):
        if self.response:
            try:
                self.url = self.response.json()['data']['url']
            except TypeError:
                logging.warning(self.response.json()['message'])
        else:
            self.url = 'https://pay.piastrix.com/en/pay'
            self.url += f'?sign={self.order.sign}&amount={self.order.amount}'
            self.url += f'&currency={self.order.currency.code}&shop_id={self.order.shop_id}&shop_order_id={self.order.id}'

    @property
    def get_currency_url(self):
        if self.order.currency.code == 840:
            self.get_response('https://core.piastrix.com/bill/create')
            self.get_url()
        elif self.order.currency.code == 643:
            self.get_response('https://core.piastrix.com/invoice/create')
            self.get_url()
        else:
            self.get_url()
        return self.url