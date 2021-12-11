#########################routes.py
from flask import render_template
from flask import Flask
import random
from .models import Quotes

from helloapp import app, db

app = Flask(__name__)
## Define below a view function 'hello', which displays the message 
## "Hello World!!! I've run my first Flask application."
## The view function 'hello' should be mapped to URL '/' .
## The view function must render the template 'index.html'
@app.route("/")
def hello():
    return "Hello World!!! I've run my first Flask application."

@app.route("/hello/<username>/")
def hello_user(username):
    quotes = [
            "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
            "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
            "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
            "Listen to many, speak to a few.",
            "Only when the tide goes out do you discover who has been swimming naked."
    ]
    return "<h2>Hello " + username + "</h2><h3>Quote of the Day for You</h3>" + random.choice(quotes)

@app.route("/quotes/")
def display_quotes():
    quotes = [
            "Only two things are infinite, the universe and human stupidity, and I am not sure about the former.",
            "Give me six hours to chop down a tree and I will spend the first four sharpening the axe.",
            "Tell me and I forget. Teach me and I remember. Involve me and I learn.",
            "Listen to many, speak to a few.",
            "Only when the tide goes out do you discover who has been swimming naked."
    ]
    return "<h1>Famous Quotes</h1><ul><li>"+ quotes[0] +"</li><li>"+ quotes[1] +"</li><li>"+ quotes[2] +"</li><li>"+ quotes[3] +"</li><li>"+ quotes[4] +"</li></ul>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


#################################### models.py
from helloapp import db
# Define Quotes model below
class Quotes(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  quoteauthor = db.Column(db.String(100), index=True)
  quotestring = db.Column(db.String(200), index=True)
  
def __repr__(self):
  return "<Quote : {}>".format(self.quotestring)
  
  #perform database migrations ????