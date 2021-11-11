from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os

dbdir = "sqlite://"+os.path.abspath(os.getcwd()) + "/database.db"

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = dbdir
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Posts(db.Model):
    # try:
    #     entore = 3.0
    #     entero = int(float(db.INT))
    # except ValueError:
    #     print("Favor ingrese un número entrero")

    try:
        
        int(db.Integer)
        it_is = True
        print("m,nvmnvbmnvbmnbvbmn")
    except ValueError:
        print("qwerqwerqwer")

        it_is = False

    print("asdfasdfasdf",it_is)
    id = db.Column(int(db.Integer), primary_key=True)
    tittle = db.Column(db.String(50))

@app.route("/")
def index():
    titulo = "Home!"
    lista = ["footer","header","info"]
    return render_template("index.html", titulo=titulo,lista=lista)
  
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)