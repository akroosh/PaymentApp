from app import app, db
from flask import render_template, request, redirect, url_for
from models import Payment


@app.route('/')
def hello_world(methods=['GET']):
    return 'Hello World!'
