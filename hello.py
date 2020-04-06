#hello.py

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    print("You are at the home page!")
    return "Hello, World!"

@app.route('/about')
def about():
    return "About me!"
