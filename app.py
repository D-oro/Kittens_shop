from flask import Flask

app = Flask(__name__)

from controllers import controller

@app.route('/')
def home():
    return "Hello there!"

if __name__ =="__main__":
    app.run(debug=True)
