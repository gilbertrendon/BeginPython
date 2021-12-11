#Aquí va la lógica
from flask import Flask
from flask import render_template, url_for, redirect
from .forms import UserForm
from helloapp import app


app = Flask(__name__)

@app.route("/adduser/")
def useradd():
   form = UserForm()
   return render_template('adduser.html', title = 'User Input Form', form = form)

if __name__ == '__main__':

    app.run()