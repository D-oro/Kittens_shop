from flask import render_template
from app import app
from models.orders import orders

@app.route("/orders")
def index():
    return render_template('index.html', title='Kittens & Cats', orders=orders)

@app.route("/orders/<index>")
def show(index):
    order = orders[int(index)]
    return render_template('show.html', order=order)