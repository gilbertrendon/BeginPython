from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", title="Title Page of Hello App")

@app.route("/a")
def helloa():
    return '''
<html>
    <head>
        <title>Title Page of Hello App</title>
    </head>
    <body>
        <h1>Hello Worlds!!!</h1>
    </body>
</html>'''

@app.route("/user/<username>/")
def hello_user(username):
    return render_template('index.html', title="User Page", user=username)

@app.route("/users/")
def display_users():

    users = ['John', 'Rosy', 'Jack', 'Sammy', 'Lilly']
    return render_template('users.html', title='Users', users=users)


if __name__ == '__main__':
    app.run()