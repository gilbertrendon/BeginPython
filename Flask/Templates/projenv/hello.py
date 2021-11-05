from flask import Flask
from flask import render_template

app = Flask(__name__)
@app.route("/")
def hello():
    return render_template("templates/index.html", title="Title Page of Hello App")

@app.route("/a")
def hello():
   return "Hello World!!!"
if __name__ == '__main__':
    app.run()