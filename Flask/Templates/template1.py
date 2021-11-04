from flask import Flask


app = Flask(__name__)

@app.route("/")
def hello():
    return '''
<html>
    <head>
        <title>Title Page of Hello App</title>
    </head>
    <body>
        <h1>Hello World!!!</h1>
    </body>
</html>'''

@app.route("/user/<username>/")
def hello_user(username):
    return '''
<html>
    <head>
       <title>User Page</title>
    </head>
    <body>
        <h1>Hello, ''' + username + '''!!!</h1>
    </body>
</html>'''


if __name__ == '__main__':
    app.run()