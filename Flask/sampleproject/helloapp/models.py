# from helloapp import db
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config  import config


app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)




class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    fname = db.Column(db.String(100), index=True)

    lname = db.Column(db.String(100), index=True)

    email = db.Column(db.String(120), index=True, unique=True)



    def __repr__(self):

        return "<User : {}>".format(self.fname+' '+self.lname)
