from flask import Flask
from flask import redirect
from flask import redirect, url_for#pa que dependiendo de una url haga algo similar al anterior

app = Flask(__name__)

@app.route("/")
def hello():
    return ("Hello World!!!")


@app.route("/user/<username>/")
def hello_user(username):
    return "Hello " + username + "!!!"

@app.route("/user/<username>/<int:age>/")
def display_age(username, age):
    return "Hello " + username +"!!!You are " + str(age) + " years old."

@app.route("/home/")
def demo_redirect():
    return redirect("http://localhost:5000/")
from flask import redirect, url_for



@app.route("/greet/user/<uname>")
def greet_user(uname):
   return redirect(url_for('hello_user', username=uname))

if __name__ == '__main__':
    app.run()