from flask import render_template
from app import app
from models.kittens import orders

@app.route("/orders")
def index():
    return render_template('index.html', title='Home', orders=orders)

@app.route("/orders/<id>")
def get_order_by_id(id):
    return render_template('order.html', order=orders[int(id)])