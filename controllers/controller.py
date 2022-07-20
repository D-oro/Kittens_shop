from flask import render_template
from app import app
from models.kittens import orders

@app.route("/orders")
def index():
    return render_template('index.html', title='Home', orders=orders)

